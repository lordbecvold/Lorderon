quest safe_box begin
	state start begin
		when 20015.chat."Otevøít Obchod" begin		
			npc.open_shop(10)
			setskin(NOWINDOW)
		end
	end
end