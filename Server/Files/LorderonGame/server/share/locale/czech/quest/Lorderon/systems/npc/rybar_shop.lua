quest safe_box begin
	state start begin
		when 9009.chat."Otev��t Obchod" begin		
			npc.open_shop(12)
			setskin(NOWINDOW)
		end
	end
end