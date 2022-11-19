class Star_Cinema:
    __hall_list = []                    #private

    def _entry_hall(self):              #protected
        self.__hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []                         # show_list = [(id,movie_name,time),.....]
        self.__rows = rows
        self.__cols = cols                             # private. if someone change the info. it will be problem.
        self.__hall_no = hall_no                       
        self._entry_hall()

    def entry_show(self, id, movie_name, time):
        tup = (id, movie_name, time)
        self.__show_list.append(tup)

        total_seat = []
        for row in range(self.__rows):
            seat = []
            for col in range(self.__cols):
                seat.append('empty')
            total_seat.append(seat)

        self.__seats[id] = total_seat

    @staticmethod
    def __is_valid_tictket(ticket,rows,colm):
        if len(ticket) != 2:
            print(f"\n\n\n\t\t{'*'*25}\tINVALID_TICKET_NO\t\t{'*'*25}\n\n\n")
            return ()
        else:
            row = ord(ticket_no[0]) - 64                    
            col = ord(ticket_no[1]) - 48
            if (row < 1 or col < 1) or (row > rows or col > colm):
                print(f"\n\n\n\t\t{'*'*25}\tINVALID TICKET\t\t{'*'*25}\n\n\n")
                return ()
            else:
                return (row,col)
            

    @staticmethod
    def __massage(name,movie_name,time,booked_seat):  #private
        print()
        print(f"{'='*27} ERROR_MASSAGE {'='*27}")
        print()
        print(f'Name: {name}')
        print()
        print(f'MOVIE_NAME: {movie_name}\tTIME: {time}\n')
        if len(booked_seat) != 0:
            print("ALREADY_BOOKED: ",end='')
            for seat in booked_seat:
                row,col = seat
                print(f"{chr(64+row)}{col}",end=' ')
        print()
        print()
        print('\t\t\tTRY AGAIN,SIR.\t\t\t')
        print('='*70,end='\n\n\n')

    @staticmethod
    def __t_massage(name,phone_no,movie_name,time,list_of_seat):    #private
        print(f"{'='*27} TICTKET INFO {'='*27}")
        print()
        print(f"TICTKET_HOLDER:{name}\n\nPHONE_NUMBER:{phone_no}\n")
        print(f'MOVIE_NAME:{movie_name}\tTIME: {time}\n')
        print("PUSCHASES SEAT_NO: ",end='')
        for seat in list_of_seat:
            row,col = seat
            print(f"{chr(64+row)}{col}",end=' ')
        print()
        print('\t\t TICTKET PURCHASES SUCCESSFUL\t\t\t')
        print('\t\t\tENJOY YOUR SHOW\t\t\t\n')
        print('='*70)
        print()
        print()
    @staticmethod
    def __is_valid_id(ID,list_of_show):
        for show in list_of_show:
            if ID in show:
                return True
        return False

    def make_tuple(self,tickets):
        return self.__is_valid_tictket(tickets,self.__rows,self.__cols)
    def valid_show_id(self,id):
        is_valid = self.__is_valid_id(id,self.__show_list)
        if not is_valid:
            print(f"\n\n\n\t\t{'*'*25}\tINVALID SHOW_ID\t\t{'*'*25}\n\n\n")
        return is_valid
    
    def book_seat(self, customer_name, phone_no, id, list_of_seat):
        is_valid_seat_no = True
        booked_seat = []
        movie_name = ''
        time = ''
        for show in self.__show_list:
            if id in show:
                movie_name = show[1]
                time = show[2]
                #list_of_seat = [(1,2),(3,4),(7,8)]
                for seat_no in list_of_seat:
                    row, col = seat_no
                    if self.__seats[id][row-1][col-1] == 'booked':
                        tup1 = (row,col)
                        booked_seat.append(tup1)
                        is_valid_seat_no = False
                if not is_valid_seat_no:
                    self.__massage(customer_name,movie_name,time,booked_seat)
                if is_valid_seat_no:
                    for seat in list_of_seat:
                        row,col = seat
                        self.__seats[id][row-1][col-1] = 'booked'
                    self.__t_massage(customer_name,phone_no,movie_name,time,list_of_seat)


    def view_show_list(self):
        print()
        print(f"{'='*37} SHOW AVAILABLE {'='*37}")
        print()
        print("MOVIE_NAME\t\t\t\tSHOW_ID\t\t\t\tTIME")
        print("----------\t\t\t\t-------\t\t\t\t----")
        i = 1
        for show in self.__show_list:
            print(f"{i}.{show[1]}\t\t{show[0]}\t\t\t{show[2]}")
            i += 1
            print()
        print('='*90)
        print()
        print()

    def view_available_seats(self, id):
        is_valid_id = self.valid_show_id(id)
        if is_valid_id:
            for show in self.__show_list:
                if id in show:
                    print()
                    print(f"{'='*43} SEAT INFORMATION {'='*44}\n")
                    print(f'MOVIE_NAME: {show[1]}\tTIME: {show[2]}')
                    print()
                    print()
                    for row in range(self.__rows):
                        for col in range(self.__cols):
                            if self.__seats[id][row][col] == 'empty':
                                print(f'{chr(65+row)}{col+1}:EMPTY\t\t', end='')
                            else:
                                print(f'X\t\t\t', end='')
                        print()
                        print()
                    print('='*104)
                    print()


# =======================================================================================



hall = Hall(5, 5, 3312)
hall.entry_show('GF101', 'Grave of The Fireflies','Nov 19 2022 04:00 PM')
hall.entry_show('LK102', 'The Lion King         ', 'Nov 19 2022 07:00 PM')
hall.entry_show('TD103', 'How to Train Your Dragon', 'Nov 19 2022 10:00 PM')


print(f"\n{'='*43} WELLCOME TO TICTKET COUNTER {'='*44}\n")
while True:
    print(f"1.VIEW ALL SHOWS\n2.VIEW AVAILABLE SEAT\n3.BOOK TICTKET\n4.EXIT\n\n")
    option = int(input('ENTER YOUR OPTION: '))
    if option == 1:
        hall.view_show_list()
    elif option == 2:        
        ID = input('ENTER SHOW ID: ')
        hall.view_available_seats(ID)
    elif option == 3:
        name = input('ENTER TICTKET BUYER NAME: ')
        phone_no = input('ENTER BUYER PHONE NUMBER: ')
        show_id = input('ENTER SHOW ID: ')
        valid = hall.valid_show_id(show_id)
        if not valid:
            continue
        tic_no = int(input('ENTER TICTKET QUANTITY: '))
        tic_list = []
        i = 1
        while i <= tic_no:
            ticket_no = input(f'ENTER TICTKET NUMBER {i}: ')              
            tup = hall.make_tuple(ticket_no)
            if not tup:
                continue
            else:
                tic_list.append(tup)
                i+=1
        hall.book_seat(name,phone_no,show_id,tic_list)
    elif option == 4:
        exit()
