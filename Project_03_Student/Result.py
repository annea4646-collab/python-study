from StudentScoreReport import StudentScoreReport

class Result:

    def __init__(self):
        self.list = StudentScoreReport()

    def start(self):
        while True:
            printMenu = input("학생이름을 입력하세요: ")

            if printMenu == '1':
                input_tool = CompanySmartPhone()
                new_data = input_tool.input_addr_data()
                self.sp.add_addr(new_data)

            elif printMenu == '2':
                input_tool = CustomerSmartPhone()
                new_data = input_tool.input_addr_data()
                self.sp.add_addr(new_data)

            elif printMenu == '3':
                self.sp.print_all_addr()

            elif printMenu == '4':
                name = input("검색할 이름을 입력하세요: ")
                self.sp.search_addr(name)

            elif printMenu == '5':
                name = input("삭제할 이름을 입력하세요: ")
                self.sp.delete_addr(name)       
                
            elif printMenu == '6':
                name = input("수정할 연락처의 이름을 입력하세요: ")
                self.sp.edit_addr(name)

            elif printMenu == '7':
                path = input("엑셀 파일 경로를 입력하세요.(xlsx): ")
                self.sp.input_from_excel(path)

            elif printMenu == '8':
                self.sp.save_data()
                print("연락처를 저장하고 프로그램을 종료합니다.")
                break
            else:
                print("메뉴 중에 선택하여 입력해주세요.")




if __name__ == "__main__":
    main_app = SmartPhoneMain()
    main_app.start()