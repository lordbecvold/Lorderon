quest reset_scroll begin
	state start begin
		when 71002.use begin

			say_title("Restartování vlastností tìla")
			say("Chceš si restartovat status postavy?") 

			local s = select("Ano", "Ne")
			if 2 == s then
				return
			end

			say_title("Restartování tìla")
			say("Chceš si je opravdu restartovat?")

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

			say_title("Reset schopností:")
			say("Tady si mùžeš nechat restartovat schopnosti.")
			say_reward("Za 1 schopnost dostaneš maximálnì 17 bodù.")

			local result = BuildSkillList(pc.get_job(), pc.get_skill_group())

			local vnum_list = result[1]
			local name_list = result[2]

			if table.getn(vnum_list) < 2 then
			say("Nemáš žádné dovednosti!")
				return
			end

			say("Jakou schopnost chceš restartovat?")

			local i = select_table(name_list)

			if table.getn(name_list) == i then
				return
			end

			local name = name_list[i]
			local vnum = vnum_list[i]

			say_title("Reset schopností:")
			say(string.format("Chceš tedy restartovat %s?", name))

			local s = select("Ano", "Ne")
			if 2 == s then
				return
			end

			say_title("Reset schopností:")
			say("Nejde to vrátit, chceš tuto schopnost")
			say("pøesto restartovat?")

			local c = select("Ano", "Ne")

			if 2 == c then
				return
			end

			local val = pc.getqf("force_to_master_skill")
			if val > 0 then
			say_title("Reset schopností:")
			say("Nemùžeš restartovat další kouzlo,")
			say("když jsi ještì nerozdìlil pøedešlé ")
				return
			end

			char_log(0, "RESET_ONE_SKILL", "USE_ITEM(71003)")
			pc.remove_item(71003)

			char_log(0, "RESET_ONE_SKILL", string.format("RESET_SKILL[%s]", name))
			pc.clear_one_skill(vnum)

			char_log(0, "RESET_ONE_SKILL", "APPLY_17MASTER_BONUS")
			pc.setqf("force_to_master_skill", 1)

			say_title("Dostal jsi 17 bodù.")
			say(string.format("%s restartován.", name))

			say_reward("Restartování schopnosti je hotovo!")
		end
	end
end