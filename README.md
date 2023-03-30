	INSTALARE  SI  DESCHIDERE  PROIECT
	
Pentru instalare is rulare proiect, se parcurg urmatorii pasi":

1. descarcare si instalare Chrome browser, deoarece proiectul de fata a fost realizat pentru utilizare cu Chrome-ul;

2. descarcare si instalare Python;

3. descarcare si instalare Pycharm Community Edition;

4. descarcare si instalare GIT;

5. in folderul unde se doreste clonarea proiectului, se da click dreapta si se selecteaza git Bash Here;

6. apoi, in fereastra deschisa, se scrie comanda git clone :  https://github.com/razvanstinghe/Final-project-QA-Automation ;

7. 	dupa descarcare, se deschide aplicatia Pycharm, iar apoi: 

a) File;
b) Open;
c) accesam calea unde s-a salvat proiectul si selectam folderul dorit;

8. 	deschidem Terminal-ul, unde vom instala urmatoarele librarii necesare rularii testelor:

a) pip install selenium + ENTER;
b) pip install webdriver-manager + ENTER;
c) pip install behave + ENTER;
d) pip install behave-html-formatter + ENTER.

Dupa rularea instalarii fiecarei librarii, se asteapta confirmarea instalarii cu succes.

9. pentru rularea testelor cu posibilitatea generarii rapoartelor, se ruleaza in Terminal comanda: 
 behave -f html -o project_report_RS.html --tags=smoke + ENTER;

10. pentru accesarea rapoartelor generate, in tree-ul proiectului:

a) se cauta fisierul cu denumirea mentionata mai sus, in cazul de fata “project_report_RS.html”;
b) click dreapta pe el;
c) Open in:
d) Browser;
e) se alege browserul dorit din lista si se asteapta deschiderea raportului.