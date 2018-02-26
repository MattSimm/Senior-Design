# Modules in this Program:
### Controller
Interact with UI, call functions in rest modules to full fill User's commond.

### UI
A graphic User interface, interact with users with button. User click bottons, UI call functions in controller to get back information. Then display the information amd provide next buttons, wait for next interaction.

### SpeechRecog
Record the conversation and convert it into string by sentence. Send the sentence to Controller.

### PersonalInfor:
turn a paragraph in to personal information, construct a string dictionary like:{'first_name':'Mary','last_name':'Smith','birth_of_date':'1990-01-01',....}

### DiagnoseInfor:
turn a paragraph in to diagnose information, construct a string dictionary like:{'diagnose':'Headache','note':'.....','medicine':'penicillin'...}.

