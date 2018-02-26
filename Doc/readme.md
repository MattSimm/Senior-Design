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
![avatar](user-case-flow.png)
The user of this software is a nurse at registration table or a doctor in the clinic, so the software is divided into two sections: Personal information section] and [Diagnose information section].

The whole interaction loop should be like this:
#### In personal information section:
A patient goes to the registration table and ask a nurse to regist him. The nurese will ask if he is new to the hospital. 
If new, nurse click new botton, UI call the controller to creat a new person information table base on the following conversation. The controller will give a parsed information back to the UI for confirmation. 
	If correct, nurse click confirm button, UI call the controller to update the person's personal imformation to database. 
	If not correct, nurse click edit button and edit the information by hand. After editing, the nurse click confirm button and does same things as before.
If not new, the nurse click find botton, type in patient's name and call the controller to find all patients with this name. The controller will return a array of patients, nurse select the right one and confirm.
The patient's id is kept for the next section, and process move to the next section.

#### In Diagnose information section:
UI call contorller to read all of the patient's information and present to doctor.
The doctor press start, UI call the controller to construct the diagnose infromation base on the following conversation. The controller will give a parsed information back to the UI for confirmation. 
	If correct, doctor click confirm button, UI call the controller to update the person's diagnose imformation to database. 
	If not correct, nurse click edit button and edit the information by hand. After editing, the nurse click confirm button and does same things as before.
The patient's id is destroyed and start a new interaction loop.

