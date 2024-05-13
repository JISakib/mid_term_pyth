class Star_Cinema:
    hall_list=[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
        super().entry_hall(self)

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)  
        self._show_list.append(show)

        self._seats[id] = [[0 for i in range(self._cols)] for j in range(self._rows)]
         

    def book_seats(self,id,seat_list):
        if id not in self._seats:
            print(f"invalid show id:{id}")
            return
        
        for row , col in seat_list:
            if row< 0 or row>=self._rows or col <0 or col>=self._cols:
                print('invalid seat')
                return

            if self._seats[id][row][col]==1:
                print(f"Seat is booked({row},{col})")
                return
            else:
                self._seats[id][row][col]=1
                print(f"Booked sit for show{id}")

    def view_show_list(self):
        for show in self._show_list:
            print(f"ID:{show[0]},movie:{show[1]},time:{show[2]}") 

    def view_available_seats(self,id):
        available_seats=[]
        if id not in self._seats:
            print(f"Didn't match show id")
            return

        for i,row in enumerate(self._seats[id]):
            for j , col in enumerate(row):
                if col ==0 :
                   available_seats.append((i,j))
        return available_seats  
     
    def print_seats(self,id):
        for row in self._seats[id]:
            print(row)

cinema_hall=Hall(5,4,1)
cinema_hall.entry_show("1","Godfather","1:00 PM")
cinema_hall.entry_show("2","Godfather","1:00 PM")
cinema_hall.entry_show("3","Godfather","3:00 PM")

while True:
    print("1:View all show")
    print("2:View available seats")
    print("3:Book a ticket ")
    print("4:Exit")
    option=input("Enter the option: ")


    if option=='1':
        cinema_hall.view_show_list()
        print('Movies list:')

    elif option=='2':
        show_id=input("Enter show ID: ")
        seats = cinema_hall.view_available_seats(show_id)
        print(f"Available seats for the show(ID:{show_id}):")
        for seat in seats:
           print(f"({seat[0]},{seat[0]})")
        cinema_hall.print_seats(show_id)
    
    elif option=='3':
        id=input('Enter show id: ')
        seat_choice=input("Enter the row coloum")
        row,col=map(int,seat_choice.split())
        seat=(row,col)
        cinema_hall.book_seats(id,[seat])
        print(f" You get the ticket . your seat{seat} for the show(Id:{id}) ")

    elif option=='4':
        break
                




         

    