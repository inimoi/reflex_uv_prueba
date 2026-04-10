import reflex as rx
import re
from ..navigation.routes import Routes
from ..utils import utils
from ..layouts.baselayout import base_layout
from ..api.auth import supabase
from .auth.login import LoginState

class ContactState(rx.State):
    """Estado para manejar el formulario de contacto y la inserción en Supabase."""
    is_loading: bool = False
    
    @rx.event
    async def handle_submit(self, form_data: dict):
        self.is_loading = True
        try:
            # Validaciones básicas
            name = form_data.get("name", "").strip()
            email = form_data.get("email", "").strip()
            
            if not name:
                return rx.toast.error("El nombre es obligatorio")
            if len(name) < 3:
                return rx.toast.error("El nombre debe tener al menos 3 caracteres")
            if not email:
                return rx.toast.error("El correo electrónico es obligatorio")
            if email:
                email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                if not re.match(email_regex, email):
                    return rx.toast.error("Por favor, introduce un correo electrónico válido")
            
            # Preparar los datos según la tabla 'contacts'
            # Campos: name, email, indicaciones
            # Nota: enviamos 'indicaciones' como lista porque en Supabase se creó como arreglo de textos (text[])
            data = {
                "name": name,
                "email": email,
            }
            
            indicaciones_text = form_data.get("indicaciones")
            if indicaciones_text:
                data["indicaciones"] = [indicaciones_text]
            
            # Insertar en la tabla 'contacts' del proyecto de Supabase
            response = supabase.table("contacts").insert(data).execute()
            
            # Verificar si la inserción fue exitosa
            if response.data:
                return [
                    rx.toast.success("¡Mensaje enviado correctamente! Nos pondremos en contacto pronto."),
                    rx.set_value("name", ""),
                    rx.set_value("email", ""),
                    rx.set_value("indicaciones", ""),
                ]
            else:
                return rx.toast.error("Error al enviar el mensaje. Inténtalo de nuevo.")
                
        except Exception as e:
            return rx.toast.error(f"Error de conexión: {str(e)}")
        finally:
            self.is_loading = False

def contact_form() -> rx.Component:
    """Componente visual del formulario de contacto con estética premium."""
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Contáctanos", size="6", margin_bottom="0.5rem", text_align="center"),
                rx.text(
                    "Rellena el formulario y el equipo te responderá lo antes posible.", 
                    color=rx.color("slate", 11), 
                    margin_bottom="1.5rem", 
                    text_align="center"
                ),
                
                # Campo Nombre
                rx.vstack(
                    rx.text("Nombre Completo*", size="2", font_weight="medium"),
                    rx.input(
                        placeholder="Tu nombre completo", 
                        name="name", 
                        id="name",
                        required=True, 
                        width="100%", 
                        variant="soft"
                    ),
                    width="100%",
                    spacing="1",
                ),
                
                # Campo Email
                rx.vstack(
                    rx.text("Correo Electrónico", size="2", font_weight="medium"),
                    rx.input(
                        placeholder="ejemplo@correo.com", 
                        name="email", 
                        id="email",
                        type="email", 
                        width="100%", 
                        variant="soft"
                    ),
                    width="100%",
                    spacing="1",
                ),
                
                # Campo Motivo / Indicaciones
                rx.vstack(
                    rx.text("Motivo del Contacto", size="2", font_weight="medium"),
                    rx.text_area(
                        placeholder="Escribe aquí el motivo de tu contacto...", 
                        name="indicaciones", 
                        id="indicaciones",
                        width="100%", 
                        variant="soft",
                        resize="vertical"
                    ),
                    width="100%",
                    spacing="1",
                ),
                
                # Botón de envío
                rx.button(
                    "Enviar Información", 
                    type="submit", 
                    width="100%",
                    loading=ContactState.is_loading,
                    color_scheme="blue",
                    padding="1.5rem",
                    margin_top="1rem",
                    cursor="pointer",
                ),
                spacing="4",
                width="100%",
            ),
            on_submit=ContactState.handle_submit,
            width="100%",
        ),
        padding="2.5rem",
        background="rgba(255, 255, 255, 0.03)",
        backdrop_filter="blur(12px)",
        border="1px solid rgba(255, 255, 255, 0.1)",
        border_radius="1.5rem",
        box_shadow="0 8px 32px 0 rgba(0, 0, 0, 0.37)",
        max_width="450px",
        width="100%",
        margin="auto",
        transition="transform 0.2s",
        _hover={"transform": "scale(1.01)"},
    )

@rx.page(
    Routes.CONTACTO.value,
    title=utils.contacto_title,
    description=utils.contacto_description,
    meta=utils.contacto_meta,
)
def contacto():
    """Página principal de contacto."""
    return base_layout(
        rx.center(
            rx.vstack(
                contact_form(),
                padding_top="4rem",
                padding_bottom="4rem",
                width="100%",
            ),
            width="100%",
        )
    )