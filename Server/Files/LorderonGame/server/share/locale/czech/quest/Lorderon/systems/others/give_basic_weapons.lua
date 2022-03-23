quest give_basic_weapon begin
    state start begin
        when login with pc.getqf("basicweapon") == 0 begin
            local klasse
            if pc.job == 0 then
                pc.give_item2(19, 1)
				pc.give_item2(12209, 1)
				pc.give_item2(11209, 1)
				pc.give_item2(3009, 1)
                klasse = "war"
            elseif pc.job == 1 then    
                pc.give_item2(1009, 1)
				pc.give_item2(12349, 1)
				pc.give_item2(11409, 1)
				pc.give_item2(2009, 1)
				pc.give_item2(8005, 1)
				pc.give_item2(19, 1)
				affect.add_collect(apply.ATTBONUS_MONSTER, 10, 60*60*24*365*60)
                klasse = "ninja"
            elseif pc.job == 2 then
				pc.give_item2(19, 1)
				pc.give_item2(12489, 1)
                pc.give_item2(11609, 1)
				affect.add_collect(apply.ATTBONUS_MONSTER, 5, 60*60*24*365*60)
                klasse = "sura"
            elseif pc.job == 3 then
                pc.give_item2(7009, 1)
				pc.give_item2(12629, 1)
				pc.give_item2(11809, 1)
				affect.add_collect(apply.ATTBONUS_MONSTER, 15, 60*60*24*365*60)
                klasse = "saman"
            end
			pc.give_item2(30201, 1)
			pc.give_item2(72726, 1)
			pc.give_item2(72730, 1)
			pc.give_item2(70007, 1)
			pc.give_item2(71164, 1)
			pc.give_item2(53006, 1)
			pc.give_item2(70038, 250)
			------------------------
			pc.give_item2(15009, 1)
			pc.give_item2(13009, 1)
			pc.give_item2(14009, 1)
			pc.give_item2(16009, 1)
			pc.give_item2(17009, 1)
			pc.give_item2(18009, 1)
			-----------------------
			affect.add_collect(apply.MOV_SPEED, 60, 60*60*24*365*60)
			affect.add_collect(apply.ATT_SPEED, 40, 60*60*24*365*60)
			ds.give_qualification()
			----------------------
			pc.set_skill_level(122,2)
			pc.set_skill_level(124,40)
			pc.set_skill_level(131,10)
			pc.set_skill_level(121,40)
			pc.set_skill_level(129,40)
			pc.set_skill_level(126,20)
			pc.set_skill_level(128,20)
			pc.set_skill_level(127,20)
			pc.set_skill_level(130,11)
            pc.setqf("basicweapon", 1)
            set_state(__complete)
        end
    end
    state __complete begin
    end
end