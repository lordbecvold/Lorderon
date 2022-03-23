quest gmstatus begin
	state start begin
		when login begin
			gmstatus.TeamMember()
			loop_timer("CheckGMActivity", 5)
		end
		
		when login with pc.is_gm() begin
			local name = pc.get_name()
			game.set_event_flag(name, 1)
			notice_all(""..name.." je online mùžete mu napsat vaše problémy a návrhy! ")
		end
		
		when logout with pc.is_gm() begin
			local name = pc.get_name()
			game.set_event_flag(name, 0)
		end
		
		when CheckGMActivity.timer begin
			gmstatus.TeamMember()
		end
		
		function TeamMember()
			local TeamMember = {
				"[Owner]Lordbecvold",
				"[COMA]Ivus",
				"[TGM]LowLike",
				"[EM]SoulStone"
				}
			local i = 1
			local TeamCount = table.getn(TeamMember) + 1
			while i < TeamCount do
				if game.get_event_flag(TeamMember[i]) == 1 then
						cmdchat("Teamler_on "..TeamMember[i])
				elseif game.get_event_flag(TeamMember[i]) == 0 then
						cmdchat("Teamler_off "..TeamMember[i])
				end
				i = i + 1
			end
		end
	end
end