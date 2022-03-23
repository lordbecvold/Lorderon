quest welcome begin
	state start begin
		when login with pc.get_playtime() == 0 begin
			say_title("Vítej na Lorderonu.")
			say("")
			say("Na zaèátek dostaneš základní výbavu, aby jsi zde pøežil.")
			say("Pøejeme ti mnoho zábavy a pevné nervy..")
            say("")
			say("Nezapomeò dodržovat pravidla!")
			say(" (Najdeš je na webu pod záložkou PRAVIDLA) ")
		end
	end
end