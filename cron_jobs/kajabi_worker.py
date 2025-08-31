# Handle the tasks in the Kajabi table and process accordingly
import logging
from datetime import datetime
from services.google_sheets import google_sheets

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def process_kajabi():
    """
    Process Kajabi tasks - currently just logs execution and updates Google Sheets
    for monitoring purposes.
    """
    start_time = datetime.now()
    logger.info("=== Starting Kajabi Worker Process ===")
    logger.info(f"Process started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Log the current task being processed
        logger.info("Processing Kajabi tasks...")
        
        # Call Google Sheets function to log execution
        spreadsheet_id = "1cF7Zdx1uwCe8yC_0i336b096l9iGXup96wUga1KOvhg"
        sheet_name = "Sheet1"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Create a log entry with timestamp
        log_data = [timestamp, "Cron Job Executed", "Kajabi Worker", "Success"]
        
        logger.info(f"Appending log entry to Google Sheets: {log_data}")
        
        # Append to Google Sheets for monitoring
        result = google_sheets.append_new_row(spreadsheet_id, sheet_name, log_data)
        
        logger.info("Successfully updated Google Sheets with execution log")
        logger.info(f"Google Sheets response: {result}")
        
        # Calculate execution time
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        logger.info(f"Process completed successfully in {execution_time:.2f} seconds")
        logger.info("=== Kajabi Worker Process Completed ===")
        
        return True
        
    except Exception as e:
        logger.error(f"Error in process_kajabi: {str(e)}")
        logger.error("=== Kajabi Worker Process Failed ===")
        
        # Try to log the error to Google Sheets
        try:
            error_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_data = [error_timestamp, "Cron Job Failed", "Kajabi Worker", f"Error: {str(e)}"]
            google_sheets.append_new_row(spreadsheet_id, sheet_name, error_data)
            logger.info("Error logged to Google Sheets")
        except Exception as sheets_error:
            logger.error(f"Failed to log error to Google Sheets: {str(sheets_error)}")
        
        return False