quest safe_box begin
	state start begin
		when 9005.chat."Otev��t sklad" begin		
			game.open_safebox()
			setskin(NOWINDOW)
		end
	end
end