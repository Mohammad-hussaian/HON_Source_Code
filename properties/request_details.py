from properties.FileType import FileType

class RequestDetails:
    def __init__(self,file_type:FileType,file_name: str, azure_search_service: str,azure_search_credentials:str):
        self.file_name= file_type
        self.file_name = file_name
        self.azure_search_credentials = azure_search_credentials
        self.azure_search_service = azure_search_service
    @property
    def file_name(self):
        retrn self._file_type
    @file_name.setter
    def file_name(self,value):
        self._file_name= value
        
    @property
    def file_type(self):
        retrn self._file_type
    @file_type.setter
    def file_type(self,value):
        self._file_type = value
    
    @property
    def azure_search_service(self):
        retrn self._azure_search_service
    @azure_search_service.setter
    def azure_search_service(self,value):
        self._azure_search_service = value
        
    @property
    def azure_search_credentials(self):
        retrn self._azure_search_credentials
    @azure_search_credentials.setter
    def azure_search_credentials(self,value):
        self._azure_search_credentials = value
        