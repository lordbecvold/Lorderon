quest lvl_120_up begin
	state start begin
		when levelup with pc.level == 120 begin
			say_title("Dok�zal jsi to!")
			say("Nade�el tv�j �as, Dok�zal jsi dokon�it maxim�ln� �rove�.")
			say(" ")
			say("D�ky tv� vytrvalosti jsi se dostal na �rove� kam m�lo kdo. ")
			say("Dra�� b�h ti gratuluje! ")
			say_yellow("Ov�em tady tv� cesta nekon��, v�k je p�eci jen ��slo. ")
			say_green(" ")
			say_green(" - Lorderon Team ti Gratuluje - ")
		end
	end
end