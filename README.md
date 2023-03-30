	INSTALARE  SI  DESCHIDERE  PROIECT
	
Pentru instalare is rulare proiect, se parcurg urmatorii pasi":

a) descarcare si instalare Chrome browser, deoarece proiectul de fata a fost realizat pentru utilizare cu Chrome-ul;

b) descarcare si instalare Python;

c) descarcare si instalare Pycharm Community Edition;

d) descarcare si instalare GIT;

e) in folderul unde se doreste clonarea proiectului, se da click dreapta si se selecteaza git Bash Here;

f) apoi, in fereastra deschisa, se scrie comanda git clone :  https://github.com/razvanstinghe/Final-project-QA-Automation ;

g) 	dupa descarcare, se deschide aplicatia Pycharm, iar apoi: File -> Open  -> accesam calea unde s-a salvat proiectul si selectam folderul dorit;

h) 	deschidem Terminal-ul, unde vom instala urmatoarele librarii necesare rularii testelor;
-pip install selenium + ENTER;
-pip install webdriver-manager + ENTER;
-pip install behave + ENTER;
-pip install behave-html-formatter + ENTER.
Dupa rularea instalarii fiecarei librarii, se asteapta confirmarea instalarii cu succes.

g) pentru rularea testelor cu posibilitatea generarii rapoartelor, se ruleaza in Terminal comanda: 
 behave -f html -o project_report_RS.html --tags=smoke + ENTER;

f) pentru accesarea rapoartelor generate, in tree-ul proiectului se cauta fisierul cu denumirea mentionata mai sus, in cazul de fata “project_report_RS.html” -> click dreapta pe el -> Open in - > Browser -> se alege browserul dorit din lista si se asteapta deschiderea raportului.


