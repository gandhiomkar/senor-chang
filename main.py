from ai.ai_model import get_ai_response, getMistakeOverview
from utils import get_or_create_user,update_user_profile

if __name__ == "__main__":
    print("Welcome to your language learning Class!")
    print("I'm Senor Chang and I'll be your instructor.")
    print("Enter your username:")
    user = get_or_create_user(input("username:").strip().lower())
    print(user.target_lang)
    
    if(user.target_lang == None):
        print("Can you tell me which language you want to learn?")
        target_lang = input("type the language you want to learn:")
        target_lang = target_lang.strip().split()[0]
        print(f"you have chosen {target_lang}")
        print(f'whats your level in {target_lang} language?:')
        print("1.Beginner \
                2.Intermediate\
                3.Advanced\
                4.Fluent\
            ")
        target_lvl_input = input("input number:")
        target_lvl_input = target_lvl_input.strip()
        match target_lvl_input:
            case '1':
                target_lvl = 'beginner'
            case '2':
                target_lvl = 'intermediate'
            case '3':
                target_lvl = 'advanced'
            case '4':
                target_lvl = 'fluent'
        print("which is your native language ?")
        native_lang = input("known language:")
        print('do you speak english? ')
        eng_lang = input('Please answer in Yes or No')
        eng_lang = eng_lang.strip().lower()
        know_eng = True if eng_lang == 'yes' else False
        print(f'target lang level:{target_lvl}')
        print(f'native lang: {native_lang}')
        print(f'knows english: {know_eng}')
        update_user_profile(user,target_lang,target_lvl,native_lang,know_eng)  

    while(True):
        user_input = input("enter message:")
        if(user_input.upper()=="END"):
            output = getMistakeOverview(user)
            print(output.content)
            break
        print(f'you: {user_input}')
        output = get_ai_response(user,user_input)
        print(f"ai: {output.reply} ({output.english_translation})")