class teacher :
    __name = "krish"
    
class principal(teacher):
    def display(self):
        print("Principal Name:", self._teacher__name) 

p = principal()
p.display()  # Output: Principal Name: krish



