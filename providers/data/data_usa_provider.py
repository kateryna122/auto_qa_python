class DataUsaProvider:

    @staticmethod
    def data_tesseract_exist():
        return {
            "module": "tesseract-olap"
        }


    @staticmethod
    def data_tesseract_non_exist():
        return {
            "module": "sadasdada"
        }

    @staticmethod
    def data_member_exist():
        return {
            "key": "04000US01",
            "caption": "Alabama"
        }

    @staticmethod
    def data_member_not_exist():
        return {
            "key": "00000UWWW",
            "caption": "AlabamaWWW"
        }