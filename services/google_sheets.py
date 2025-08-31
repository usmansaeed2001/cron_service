from google.oauth2 import service_account
from googleapiclient.discovery import build
import base64
import json
import os

from config.system import GoogleConfig

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


class GoogleSheetsService:
    """
    Singleton class for Google Sheets operations.
    """
    _instance = None
    _service = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GoogleSheetsService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            b64_creds = GoogleConfig.b64_creds
            if b64_creds is None:
                raise ValueError("GOOGLE_SERVICE_CREDENTIALS is not set")
            info = json.loads(base64.b64decode(b64_creds))
            credentials = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
            self._service = build('sheets', 'v4', credentials=credentials)

    def _get_service(self):
        """Get the already initialized Google Sheets service."""
        return self._service

    def append_new_row(self, spreadsheet_id, sheet_name="Sheet1", values=None):
        """
        Add a new row to the bottom of the specified sheet.
        
        Args:
            spreadsheet_id (str): Google Sheets spreadsheet ID
            sheet_name (str): The name of the sheet/tab to append to. Defaults to "Sheet1"
            values (list): List of values to append as a new row. If None, appends empty row
            
        Returns:
            dict: The response from Google Sheets API
        """
        if values is None:
            values = []
        
        # Ensure values is a list of lists (each inner list represents a row)
        if not isinstance(values, list):
            values = [values]
        if values and not isinstance(values[0], list):
            values = [values]
        
        service = self._get_service()
        sheet = service.spreadsheets()
        
        # Use the append method to add rows to the bottom
        body = {'values': values}
        result = sheet.values().append(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A:A",  # Append to column A (will auto-expand)
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',  # Insert new rows
            body=body
        ).execute()
        
        return result


# Global instance for easy access
google_sheets = GoogleSheetsService()
