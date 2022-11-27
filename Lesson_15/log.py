import logging
import Task_1_server_from_Lesson_11


def main():

    logger = logging.getLogger("log_from.Task_1_server_from_Lesson_11")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("server.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = Task_1_server_from_Lesson_11.server()

    logger.info("Done!")

    logger.warning()


if __name__ == "__main__":
    main()
