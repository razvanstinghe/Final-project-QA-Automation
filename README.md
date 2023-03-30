	INSTALARE  SI  DESCHIDERE  PROIECT
	
Pentru instalare is rulare proiect, se parcurg urmatorii pasi":

a) descarcare si instalare Chrome browser, deoarece proiectul de fata a fost realizat pentru utilizare cu Chrome-ul;

b) descarcare si instalare Python;

c) descarcare si instalare Pycharm Community Edition;

d) descarcare si instalare GIT;

e) in folderul unde se doreste clonarea proiectului, se da click dreapta si se selecteaza git Bash Here;

f) apoi, in fereastra deschisa, se scrie comanda git clone :  https://github.com/razvanstinghe/Final-project-QA-Automation ;

g) 	dupa descarcare, se deschide aplicatia Pycharm, iar apoi: 
1. File;
2. Open;
3. accesam calea unde s-a salvat proiectul si selectam folderul dorit;

h) 	deschidem Terminal-ul, unde vom instala urmatoarele librarii necesare rularii testelor:
1. pip install selenium + ENTER;
2. pip install webdriver-manager + ENTER;
3. pip install behave + ENTER;
4. pip install behave-html-formatter + ENTER.
Dupa rularea instalarii fiecarei librarii, se asteapta confirmarea instalarii cu succes.

g) pentru rularea testelor cu posibilitatea generarii rapoartelor, se ruleaza in Terminal comanda: 
 behave -f html -o project_report_RS.html --tags=smoke + ENTER;

f) pentru accesarea rapoartelor generate, in tree-ul proiectului:
1. se cauta fisierul cu denumirea mentionata mai sus, in cazul de fata “project_report_RS.html”;
2. click dreapta pe el;
3. Open in - > Browser -> se alege browserul dorit din lista si se asteapta deschiderea raportului.