import logging
import sys
from datetime import datetime
from cron_jobs.kajabi_worker import process_kajabi

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('cron_service.log')
    ]
)
logger = logging.getLogger(__name__)

def main():
    """
    Main entry point for the cron service.
    Executes the Kajabi worker process and handles any errors.
    """
    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("CRON SERVICE STARTED")
    logger.info(f"Service started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)
    
    try:
        # Execute the Kajabi worker process
        success = process_kajabi()
        
        if success:
            logger.info("Cron service completed successfully")
        else:
            logger.error("Cron service failed")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Unexpected error in main: {str(e)}")
        logger.error("Cron service failed with unexpected error")
        sys.exit(1)
    
    finally:
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        logger.info(f"Total execution time: {total_time:.2f} seconds")
        logger.info("=" * 60)
        logger.info("CRON SERVICE ENDED")
        logger.info("=" * 60)

if __name__ == "__main__":
    main()