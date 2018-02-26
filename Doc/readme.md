# Modules in this Program:
### Controller
Interact with UI, call functions in rest modules to full fill User's commond.

### UI
A graphic User interface, interact with users with button. User click bottons, UI call functions in controller to get back information. Then display the information amd provide next buttons, wait for next interaction.

### SpeechRecog
Record the conversation and convert it into string by sentence. Send the sentence to Controller.

### PersonalInfor:
Turn a paragraph in to personal information, construct a string dictionary like:{'first_name':'Mary','last_name':'Smith','birth_of_date':'1990-01-01',....}

### DiagnoseInfor:
Turn a paragraph in to diagnose information, construct a string dictionary like:{'diagnose':'Headache','note':'.....','medicine':'penicillin'...}.

### Database:
Connect with our EMR database, read a patients record when asked by controller, update the EMR database when new information for a patient is ready.


# User Interaction in UI
The user of this software is a nurse at registration table or a doctor in the clinic.
The whole interaction loop should be like this:
A patient go to the registration table and ask a nurse to regist him. The nurese will ask if he is new to the hospital. If new, nurse click new botton, UI call the controller to creat a new person information table base on the following conversation. The controller will give a parsed information back to the UI for confirmation. If correct, nurse click confirm button, UI call the controller to update the person's personal imformation.

