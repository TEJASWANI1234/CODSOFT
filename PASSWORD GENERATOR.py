import secrets
import string

class passwordGenerator:
    def __init__(self):
        self.com_level={
            'low':string.ascii_letters+string.digits,
            'medium':string.ascii_letters+string.digits+string.punctuation,
            'high':string.ascii_letters+string.digits+string.punctuation+string.ascii_letters.upper()+string.punctuation
            }
    

    def generate_password(self,length,complexity='medium'):
        characters = self.com_level.get(complexity)
        if not characters:
            raise ValueError ("invalid choose 'low' or 'medium'or 'high'") 
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

def user_input():
    length = int(input("Enter the desired length of the password: "))
    complexity=input("enter the complexity level(low,medium,high):").lower()
    return length,complexity


def display_password(password):
    print("generated password:",password)

def main():
    password_generated =passwordGenerator()

    try:
        length,complexity=user_input()
        generated_password=password_generated.generate_password(length,complexity)
        display_password(generated_password)    
     
    except ValueError as e:
        print(f"Error :{e}")
if __name__ == "__main__":
    main()
