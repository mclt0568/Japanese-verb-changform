#Copyright(c) 2019 mclt0568. MIT LISENCE applied.
#core functions, methods and classes goes here
import predefined

#Object_Class for different forms of verbs
class defforms:
	def __init__(self,nai:str="",dictionary:str="",te:str=""):
		self.nai=nai
		self.dictionary = dictionary
		self.te = te

#Object_Class for different verbs
class verbclass:
	def __init__(self,root:str,masu:str,group:int,forms:defforms=defforms(nai="",dictionary="",te="")):
		self.root = root
		self.masu = masu
		self.group = group
		self.forms = forms

#Function_Class for operation of verbs for sorting
class operation:
	#Count the pronounces in the hiraganas
	def countprn(verb:str):
		for i in list(verb):
			if not(i in predefined.hiragana):
				excep(verb,"Non-Hinagara found, please use Hinagara ONLYY")
				return False
		else:
			for i in ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ"]:
				verb = verb.replace(i,"")
			return len(list(verb))

	#Check if verb is written in Hiragana only and is masu-form
	def checkvalid(verb:str):
		for i in list(verb):
			if not(i in predefined.hiragana):
				excep(verb,"Non-Hinagara found, please use Hinagara ONLYY")
				return False
		if verb.strip() == "":
			return False
		if not (verb[-2:] =="ます"):
			excep(verb,"Not ます-form, Please makesure the verb ends with ます")
			return False
		if operation.countprn(verb) < 3:
			excep(verb,"Needs to be more then 5 pronounsations.")
			return False
		return True
	def remove_masu(verb_with_masu:str):
		if verb_with_masu[-2:] =="ます":
			return verb_with_masu[:-2]
		else:
			excep(verb_with_masu,"Not ます-form, Please makesure the verb ends with ます")

#Process and give reason for error occured
def excep(error:str,errstr:str):
	print("\nerror occured on '{}' \ndue to the following reason \n{}\n".format(errstr,error))

#sort verb in masu form and returns a group as int, returns None if not valid
def sorttogroup(verb_in_masu_form:str):
	global operation
	verb = verb_in_masu_form.strip()
	_verb = operation.remove_masu(verb)
	group = 0
	if operation.checkvalid(verb):
		if verb in  ["します","きます"]:
			group = 3
		elif operation.countprn(_verb) == 1:
			group = 2
		elif (_verb[-1]  == "し") and (operation.countprn(verb) >= 5):
			group = 3
		elif (_verb[-1] in predefined.sortedhiragana.i):
			group = 1
		else:
			group = 2
		return group
	else:
		return None

#sort verb in masu form by groups and returns a verb object, returns None if not valid
def sorttoverb(verb_in_masu_form:str):
	global operation
	verb = verb_in_masu_form.strip()
	_verb = operation.remove_masu(verb)
	if operation.checkvalid(verb):
		if sorttogroup(verb) == 1:
			nai = _verb[:-1]+predefined.sortedhiragana.torow(_verb[-1],"a") + "ない"
			dictionary = _verb[:-1]+predefined.sortedhiragana.torow(_verb[-1],"u")
			if _verb[-1] in ("い","ち","り"):
				te = _verb[:-1]+"って"
			elif _verb[-1] in ("み","に","び"):
				te = _verb[:-1]+"んで"
			elif _verb == "いき":
				te = "いって"
			elif _verb[-1] == "き":
				te = _verb[:-1]+"いて"
			elif _verb[-1] == "ぎ":
				_verb[:-1]+"っで" 
		elif sorttogroup(verb) == 2:
			nai = _verb + "ない"
			dictionary = _verb + "る"
			te = _verb+"て"
		elif sorttogroup(verb) == 3:
			if verb[-3:] == "します":
				nai = verb[:-3] +"しない"
				dictionary =  verb[:-3] +"する"
				te =  verb[:-3] +"して"
			else:
				nai =  _verb[:-3] +"こない"
				dictionary =  _verb[:-3] + "くる"
				te = _verb[:-3] +"きて"
		return verbclass(_verb,verb,sorttogroup(verb),defforms(nai=nai,dictionary=dictionary,te=te))
			
	else:
		return None

#Print out the text in a nice orgenized way
def showresult(verbobj:verbclass):
	print("Result for {}:\nGroup: {}\nNai-form: {}\nDictionary-form: {}\nTe-form: {}".format(verbobj.masu,verbobj.group,verbobj.forms.nai,verbobj.forms.dictionary,verbobj.forms.te))