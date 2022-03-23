quest reset_scroll begin
	state start begin
		when 71002.use begin

			say_title("Restartov�n� vlastnost� t�la")
			say("Chce� si restartovat status postavy?") 

			local s = select("Ano", "Ne")
			if 2 == s then
				return
			end

			say_title("Restartov�n� t�la")
			say("Chce� si je opravdu restartovat?")

			local c = select("Ano", "Ne")
			if 2 == c then
				return
			end

			char_log(0, "RESET_ALL", "USE_ITEM(71002)")
			pc.remove_item(71002)

			char_log(0, "RESET_ALL", "RESET_STAT_POINTS")
			pc.reset_point()
		end

		when 71003.use begin

			say_title("Reset schopnost�:")
			say("Tady si m��e� nechat restartovat schopnosti.")
			say_reward("Za 1 schopnost dostane� maxim�ln� 17 bod�.")

			local result = BuildSkillList(pc.get_job(), pc.get_skill_group())

			local vnum_list = result[1]
			local name_list = result[2]

			if table.getn(vnum_list) < 2 then
			say("Nem� ��dn� dovednosti!")
				return
			end

			say("Jakou schopnost chce� restartovat?")

			local i = select_table(name_list)

			if table.getn(name_list) == i then
				return
			end

			local name = name_list[i]
			local vnum = vnum_list[i]

			say_title("Reset schopnost�:")
			say(string.format("Chce� tedy restartovat %s?", name))

			local s = select("Ano", "Ne")
			if 2 == s then
				return
			end

			say_title("Reset schopnost�:")
			say("Nejde to vr�tit, chce� tuto schopnost")
			say("p�esto restartovat?")

			local c = select("Ano", "Ne")

			if 2 == c then
				return
			end

			local val = pc.getqf("force_to_master_skill")
			if val > 0 then
			say_title("Reset schopnost�:")
			say("Nem��e� restartovat dal�� kouzlo,")
			say("kdy� jsi je�t� nerozd�lil p�ede�l� ")
				return
			end

			char_log(0, "RESET_ONE_SKILL", "USE_ITEM(71003)")
			pc.remove_item(71003)

			char_log(0, "RESET_ONE_SKILL", string.format("RESET_SKILL[%s]", name))
			pc.clear_one_skill(vnum)

			char_log(0, "RESET_ONE_SKILL", "APPLY_17MASTER_BONUS")
			pc.setqf("force_to_master_skill", 1)

			say_title("Dostal jsi 17 bod�.")
			say(string.format("%s restartov�n.", name))

			say_reward("Restartov�n� schopnosti je hotovo!")
		end
	end
end