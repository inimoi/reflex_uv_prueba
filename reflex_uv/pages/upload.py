import reflex as rx
from ..layouts.baselayout import base_layout
from ..navigation.routes import Routes
# from ..api.auth import supabase  # No longer needed here
from ..utils import utils
import httpx
import os


class UploadState(rx.State):
    """The app state for the upload page."""
    
    is_uploading: bool = False
    upload_status: str = ""
    
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s) via the FastAPI endpoint."""
        self.is_uploading = True
        self.upload_status = "Subiendo archivo..."
        
        # URL del backend (FastAPI)
        # En Reflex, por defecto el backend corre en el puerto 8000
        backend_url = os.getenv("API_URL", "http://localhost:8000")
        upload_endpoint = f"{backend_url}/upload"
        
        async with httpx.AsyncClient() as client:
            for file in files:
                upload_data = await file.read()
                file_name = file.filename
                
                try:
                    # Preparar el archivo para el POST request
                    files_payload = {
                        "file": (file_name, upload_data, file.content_type)
                    }
                    
                    # Llamar al endpoint de FastAPI
                    response = await client.post(upload_endpoint, files=files_payload)
                    result = response.json()
                    
                    if response.status_code == 200 and result.get("success"):
                        self.upload_status = f"✅ {result.get('message')}"
                    else:
                        error_type = result.get("error")
                        if error_type == "duplicate":
                            self.upload_status = f"⚠️ {result.get('message')}"
                        else:
                            self.upload_status = f"❌ {result.get('message')}"
                            
                except Exception as e:
                    print(f"Error calling API: {e}")
                    self.upload_status = f"❌ Error de conexión: {str(e)}"
                
        self.is_uploading = False

@rx.page(route=Routes.UPLOAD.value, 
    title=utils.upload_title,
    description=utils.upload_description,
    meta=utils.upload_meta)
def upload_page() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("Sube tus Fotos", size="8", margin_bottom="2rem"),
            
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Seleccionar Archivos",
                        color_scheme="blue",
                        variant="solid",
                    ),
                    rx.text(
                        "Arrastra los archivos aquí o haz clic para seleccionar",
                        color="gray",
                    ),
                     rx.text(
                        "Admita archivos JPG, PNG, GIF y WEBP",
                        color="gray",
                    ),
                    align_items="center",
                    justify_content="center",
                    padding="2rem",
                    border="2px dashed",
                    border_color=rx.color("blue", 5),
                    border_radius="md",
                    _hover={"bg": rx.color("blue", 2)},
                ),
                id="photo_upload",
                multiple=True,
                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"],
                    "image/gif": [".gif"],
                    "image/webp": [".webp"],
                },
                max_files=5,
                disabled=UploadState.is_uploading,
                on_drop=UploadState.handle_upload(rx.upload_files(upload_id="photo_upload")),
            ),
            
            rx.cond(
                UploadState.is_uploading,
                rx.spinner(size="3"),
            ),
            
            rx.text(
                UploadState.upload_status,
                color=rx.cond(
                    UploadState.upload_status.contains("Error") | UploadState.upload_status.contains("⚠️"),
                    rx.color("red", 9),
                    rx.color("green", 9),
                ),
                weight="bold",
                margin_top="1rem",
            ),
            
            align_items="center",
            width="100%",
            padding_top="4rem",
        )
    )
