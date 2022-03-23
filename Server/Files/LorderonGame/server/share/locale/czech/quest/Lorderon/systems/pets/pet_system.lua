quest pet_system begin
    state start begin
        function get_pet_info(itemVnum)
            pet_info_map = {
			-------------------------------------------------------------
                [53006]     = { 34006, " Rufus", 0},
				[53008]     = { 34005, " Porky", 0},
				[53010]     = { 34008, " Leonidas", 0},
				[53014]     = { 34013, " Mini-executor", 0},
				[55702]     = { 34045, " Mini-Pavouèek", 0},
				[55703]     = { 34049, " Mini-Razador", 0},
			-------------------------------------------------------------
            }

            itemVnum = tonumber(itemVnum)

            return pet_info_map[itemVnum]
        end
		function get_spawn_effect_file(idx)
			effect_table = {
				[0] = nil,
				[1] = "d:\\\\ymir work\\\\effect\\\\etc\\\\appear_die\\\\npc2_appear.mse",
			}
			return effect_table [idx]
		end
        when 
		------------------------------------------------------------------
		53006.use or 53008.use or 53010.use or 53014.use or 55702.use or 55703.use
		------------------------------------------------------------------
		begin
            local pet_info = pet_system.get_pet_info(item.vnum)

            if null != pet_info then

                local mobVnum = pet_info[1]
                local petName = pet_info[2]
				local spawn_effect_file_name = pet_system.get_spawn_effect_file(pet_info[3])

                if true == pet.is_summon(mobVnum) then
					if spawn_effect_file_name != nil then
						pet.spawn_effect (mobVnum, spawn_effect_file_name)
					end
                    pet.unsummon(mobVnum)
                else
                    if pet.count_summoned() < 1 then
                        pet.summon(mobVnum, petName, false)
                    end
					if spawn_effect_file_name != nil then
						pet.spawn_effect(mobVnum, spawn_effect_file_name)
					end
                end
            end
        end
    end
end
