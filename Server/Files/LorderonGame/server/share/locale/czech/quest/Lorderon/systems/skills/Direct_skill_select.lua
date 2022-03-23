quest directskills begin
	state start begin
		when login or levelup with pc.level >= 5 begin
			if pc.get_skill_group() == 0 and pc.getqf("skills", 0) then
				set_state(run)
			end
		end
	end
	state run begin
		when letter with pc.getqf("skills") == 0 begin
			send_letter("Vyber si cestu ")
		end
		when button or info with pc.getqf("skills") == 0 begin
			local all = {
				[0] = {"Tìlesný boj ", "Mentální boj "},
				[1] = {"Boj z blízka ", "Boj na dálku "},
				[2] = {"Magické zbranì ", "Èerná magie "},
				[3] = {"Draèí moc ", "Léèba "},
			}
		--------------------------------------------		
			local skill = {
				[0]={
					[1]={1, 2, 3, 4, 5},
					[2]={16, 17, 18, 19, 20},
				},
				[1]={
					[1]={31, 32, 33, 34, 35},
					[2]={46, 47, 48, 49, 50},
				},
				[2]={
					[1]={61, 62, 63, 64, 65, 66},
					[2]={76, 77, 78, 79, 80, 81},
				},
				[3]={
					[1]={91, 92, 93, 94, 95, 96},
					[2]={106, 107, 108, 109, 110, 111}
				},
			}
		---------------------------------------------
			say_title("Vyber si cestu: ")
			say("Toto rozhodnutí je koneèné a nelze zmìnit. ")
			say("Tak co to bude ? ")
			local a = select(all[pc.get_job()][1], all[pc.get_job()][2], "Rozhodnu se pozdìji. ")
			if a == 1 or a == 2 then
				pc.set_skill_group(tonumber(a))
				pc.clear_skill()
				clear_letter()
				for i = 1, table.getn(skill[pc.get_job()][pc.get_skill_group()]) do
					pc.set_skill_level (skill[pc.get_job()][pc.get_skill_group()], 40)
				end
				pc.setqf("skills", 1)
			elseif a == 3 then
				return
			end
		end
	end
end 