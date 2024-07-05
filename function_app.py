from properties.request_details import RequestDetails
from properties.filetype import FileType
details = RequestDetails(file_type = FileType ,
                        file_name: str,
                        azure_search_service: str,
                        azure_search_credentials:str,
                        )
file_type_maping = {
                    "document_delete": FileType.delete,
                    "docuement_update":FileType.update,
                     "document_create":document_trasformer
                    }