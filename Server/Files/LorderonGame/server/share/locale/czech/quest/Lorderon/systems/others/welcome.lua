quest welcome begin
	state start begin
		when login with pc.get_playtime() == 0 begin
			say_title("V�tej na Lorderonu.")
			say("")
			say("Na za��tek dostane� z�kladn� v�bavu, aby jsi zde p�e�il.")
			say("P�ejeme ti mnoho z�bavy a pevn� nervy..")
            say("")
			say("Nezapome� dodr�ovat pravidla!")
			say(" (Najde� je na webu pod z�lo�kou PRAVIDLA) ")
		end
	end
end