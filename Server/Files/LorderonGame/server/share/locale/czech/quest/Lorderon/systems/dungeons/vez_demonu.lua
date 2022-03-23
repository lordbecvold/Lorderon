quest deviltower_zone begin
    state start begin
	when login begin
	    if pc.get_map_index() == 66 then
		-- Vrstvy kategorie 
		-- 1F   88  577  236 737
		-- 2F   91  343  238 504
		-- 3F  104  107  248 269
		if pc.get_x() < 2048+88 or pc.get_y() < 6656+577 or pc.get_x() > 2048+236 or pc.get_y() > 6656+737 then
		    pc.warp((5376+532)*100, (512+596+4)*100, 65)
		end
		pc.set_warp_location(65, 5376+532, 512+596+4)
	    elseif pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 then
		pc.set_warp_location(65, 5376+532, 512+596+4)
	    end
	end
	when 20348.click begin
	    if pc.get_level() < 40 then
		say("Mnoho lidí v této vei našlo smrt. ")
		say("Jsi moc slabı, musíš mít minimálne 40 level. ")
		say()
	    else
		say("V této vei je sposta dáblu. ")
		say("Jenom ti nejsilnejší se dostanou a na vrchol vee.")
		say("Ale ríká se, e kdo vleze do vee, tak u nevyleze.")
		say("Chceš i presto vstoupit do vee? ")
		local s= select("Ano ", "Ne")
		if s == 1 then
		    -- warp into!
		    pc.warp(216500,727000)
		end
	    end
	end
	when devil_stone1.kill begin
	    timer("devil_stone1_1", 5)
	end
	when devil_stone1_1.timer begin
		local mapto7= pc.count_item(30302)  -- To neni pravda, vyhlazeni dusi ve vezi  
		pc.remove_item(30302,mapto7)

		local boxto7= pc.count_item(30300)  -- Neodstrani nezname, jedna se o pole 
		pc.remove_item(30300,boxto7)

	    d.new_jump_all(66, special.devil_tower[1][1], special.devil_tower[1][2])
	    d.regen_file("data/dungeon/deviltower2_regen.txt")
	    d.set_warp_at_eliminate(4, d.get_map_index(), special.devil_tower[2][1], special.devil_tower[2][2], "data/dungeon/deviltower3_regen.txt")
	end
	--when devil_stone2.kill begin
	--d.jump_all_local(special.devil_tower[2][1], special.devil_tower[2][2])
	--end
	when devil_stone3.kill begin
	    --d.jump_all_local(special.devil_tower[3][1], special.devil_tower[3][2])
	    --d.set_exit_all_at_eliminate(6)
	    --d.set_warp_at_eliminate(6, d.get_map_index(), 100, 100)
	    --d.set_warp_at_eliminate(4, 65, 5376+532, 512+596+4)
	    d.set_warp_at_eliminate(4, d.get_map_index(), special.devil_tower[3][1], special.devil_tower[3][2], "data/dungeon/deviltower4_regen.txt")
	    d.check_eliminated()
	    --d.exit_all()
	end
	function get_4floor_stone_pos()
	    local positions = {
		{368, 629},
		{419, 630},
		{428, 653},
		{422, 679},
		{395, 689},
		{369, 679},
		{361, 658},
	    }
	    for i = 1, 6 do
		local j = number(i, 7)
		if i != j then
		    local t = positions[i];
		    positions[i] = positions[j];
		    positions[j] = t;
		end
	    end
	    --for i = 1, 7 do
	--	positions[i][1] = positions[i][1] * 100
	--	positions[i][2] = positions[i][2] * 100
	 --   end
	    return positions
	end
	when 8016.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
	    d.setf("level", 4)
	    -- Zniè správné kameny Metin. 
	    --d.regen_file("data/dungeon/deviltower4_regen.txt")
	    local positions = deviltower_zone.get_4floor_stone_pos()
	    for i = 1, 6 do
		chat(positions[i][1], positions[i][2])
		d.set_unique("fake" .. i , d.spawn_mob(8017, positions[i][1], positions[i][2]))
	    end
	    chat(positions[7][1], positions[7][2])
	    local vid = d.spawn_mob(8017, positions[7][1], positions[7][2])
	    chat(vid)
	    d.set_unique("real", vid)
	    server_loop_timer('devil_stone4_update', 10, pc.get_map_index())
	    server_timer('devil_stone4_fail1', 20*60, pc.get_map_index())

	    d.notice("Zde je 4. patro,");
	    d.notice("máš 20 minut na to,");
	    d.notice("abys znièil spravnı Šutr.");
	end

	when devil_stone4_fail1.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Máš ještì 15 minut.")
		server_timer('devil_stone4_fail2', 15*60, get_server_timer_arg())
	    end
	end

	when devil_stone4_fail2.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Máš jestì 10 minut.")
		server_timer('devil_stone4_fail', 10*60, get_server_timer_arg())
	    end
	end

	when devil_stone4_fail.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Došel ti èas.")
		d.exit_all()
		clear_server_timer('devil_stone4_update', get_server_timer_arg())
	    end
	end

	when devil_stone4_update.server_timer begin
	    if d.select(get_server_timer_arg()) then
		if not d.is_unique_dead("real") then
		    for i = 1, 6 do
			if d.getf("fakedead" .. i) == 0 then
			    if d.unique_get_hp_perc("fake" .. i) < 50 then
				d.purge_unique("fake" .. i)
				d.setf("fakedead" .. i, 1)
				d.notice("Špatné šutry zmizí.");
			    end
			end
		    end
		else
		    --d.clear_regen()
		    --d.regen_file("data/dungeon/deviltower5_regen.txt")
		    server_timer("devil_stone4_end", 5, get_server_timer_arg())
		    d.notice("Gratuluji, podaøilo se ti znièit spravnı Šutr,");
		    d.notice("pokraèuješ do dalšího patra.")
		    clear_server_timer('devil_stone4_fail1', get_server_timer_arg())
		    clear_server_timer('devil_stone4_fail2', get_server_timer_arg())
		    clear_server_timer('devil_stone4_fail', get_server_timer_arg())
		end
	    else
		server_timer('devil_stone4_stop_timer', 1, get_server_timer_arg())
	    end
	end

	when devil_stone4_stop_timer.server_timer begin
	    clear_server_timer('devil_stone4_update', get_server_timer_arg())
	end

	when devil_stone4_end.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.setf("level", 5)
		d.setf("stone_count", 5)
		d.notice("Vítej v 5. patøe")
		d.notice("Zabíjej pøišery, dokud ti z nich nespadnou")
		d.notice("klíèe, které odemknou peèetì.")
		d.notice("Na otevøení všech peèetí máš 30 minut.")
		d.jump_all(special.devil_tower[4][1], special.devil_tower[4][2])
		server_timer('devil_stone5_fail1', 30*60, get_server_timer_arg())
		clear_server_timer('devil_stone4_update', get_server_timer_arg())

		-- 5. Akcie nadále reprudukovat
		d.set_regen_file("data/dungeon/deviltower5_regen.txt")

		-- 5. Skladem, Seal Stone reprodukce
		d.spawn_mob(20073, 421, 452)
		d.spawn_mob(20073, 380, 460)
		d.spawn_mob(20073, 428, 414)
		d.spawn_mob(20073, 398, 392)
		d.spawn_mob(20073, 359, 426)
	    end
	end
	when devil_stone5_fail1.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Zbıvá ještì 20 minut.")
		server_timer('devil_stone5_fail2', 20*60, get_server_timer_arg())
	    end
	end

	when devil_stone5_fail2.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Zbıvá ještì 15 minut.")
		server_timer('devil_stone5_fail3', 15*60, get_server_timer_arg())
	    end
	end

	when devil_stone5_fail3.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Zbıvá ještì 10 minut.")
		server_timer('devil_stone5_fail', 10*60, get_server_timer_arg())
	    end
	end

	when devil_stone5_fail.server_timer begin
	    if d.select(get_server_timer_arg()) then
		d.notice("Došel ti èas.")
		d.exit_all()
	    end
	end

	--when devil_stone4.kill begin
	    --d.setf("level", 5)
	    --d.setf("stone_count", 4)
	    --d.clear_regen()
	    --d.regen_file("data/dungeon/deviltower5_regen.txt")
	    --d.jump_all_local(special.devil_tower[4][1], special.devil_tower[4][2])
	--end

	when 1062.kill with pc.in_dungeon() and d.getf("level") == 5 begin
	    local KILL_COUNT_FOR_DROP_KEY = 1
	    --if is_test_server() then
		--KILL_COUNT_FOR_DROP_KEY = 1
	    --end
	    local n =d.getf("count") + 1
	    d.setf("count", n) 
	    if n == KILL_COUNT_FOR_DROP_KEY then
		-- Falling Tasten 
		game.drop_item(50084, 1)
		d.setf("count", 0)
	    end
	end
	when devil_stone5.take with item.vnum == 50084 begin
	    npc.purge()
	    item.remove()
	    d.setf("stone_count", d.getf("stone_count") - 1)
	    if d.getf("stone_count") <= 0 then
		d.setf("level", 6)
		d.clear_regen()
		d.regen_file("data/dungeon/deviltower6_regen.txt")

		d.notice("Gratuluji, povedlo se ti otevøít")
		d.notice("všechny peèetì.")
		d.jump_all(special.devil_tower[5][1], special.devil_tower[5][2])
		clear_server_timer('devil_stone5_fail1', get_server_timer_arg())
		clear_server_timer('devil_stone5_fail2', get_server_timer_arg())
		clear_server_timer('devil_stone5_fail3', get_server_timer_arg())
		clear_server_timer('devil_stone5_fail', get_server_timer_arg())
	    else
		d.notice("Odstranil jsi jeden sloup, jestì tì zbıvá odstranit "..d.getf("stone_count").." sloupy.")
	    end
	end

	when devil_stone6.kill begin
	    -- Zabij všechny pøíšery 
	    -- a pak zabij bosse. 
	    --d.jump_all(special.devil_tower[6][1], special.devil_tower[6][2])
	    d.kill_all()
	   -- d.set_warp_at_eliminate(3*60, 65, 5376+532, 512+596+4)
	    d.check_eliminated()
	    local reward_alchemist = {20074, 20075, 20076}
	    d.spawn_mob(reward_alchemist[number(1,3)], 425, 216);
	    d.spawn_mob(20083, 427, 214);
	    d.setqf("can_refine", 1)
	end

	when 20083.chat."Další patro" with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		say(""..mob_name(20083).."")
		say("Ty chceš do dalšího patra?")
		say("Uvidím jestli to pùjde.")
		say("")
		wait()
		if pc.level >=75 then
			say("Dobøe, vemu tì ")
			say("do 7. patra.")
			timer("devil_jump_7", 6)
			return
		end
		say("Máš moc malı level, a proto tì ")
		say("pøesunu pryè odsud.")
		say("")
		wait()
		pc.warp(590500, 110500)
		return
    end

   when devil_jump_7.timer begin
		d.clear_regen()

		d.spawn_mob(8018, 639, 658)
		d.spawn_mob(8018, 611, 637)
		d.spawn_mob(8018, 596, 674)
		d.spawn_mob(8018, 629, 670)

		d.setf("level", 7)

		d.jump_all(2048+590, 6656+638)
	end
	
	when 8018.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		local cont = d.getf("7_stone_kill") + 1
		d.setf("7_stone_kill", cont)

		if cont >= 4 then
			d.setf("7_stone_kill", 0)
			d.set_regen_file("data/dungeon/deviltower7_regen.txt")
		end	
	end

	when 8019.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		game.drop_item(30300, 1)
	end

	when 30300.use with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		pc.remove_item("30300", 1)

		local pct = number(1,10)

		if pct == 1 then
			-- Karta platí 
			game.drop_item(30302, 1)
			d.clear_regen()
		else
			-- Karta platí 
			game.drop_item(30302, 1)
			
		end
	end

	when 30302.use with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		-- An der 8th Floor 
		say("Našel jsi správnou mapu,")
		say("a proto tì pøesunu do dalšího patra.")
		pc.remove_item("30302", 1)
	    timer("devil_jump_8", 6)
		d.clear_regen()
	end
						
	--------------------------------------------
	-- Von 8 F vor der Ankunft geben Sie die 9 F 
	--------------------------------------------
	when devil_jump_8.timer begin
		d.setf("level", 8)
		d.jump_all(2048+590, 6656+403)
		d.set_regen_file("data/dungeon/deviltower8_regen.txt")
		d.spawn_mob(20366, 640, 460)
		local _count= pc.count_item(30302)-- True Tilgung Dead Turm 
		pc.remove_item(30302,_count)
		
	end

	when 1040.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		local pct1 = number(1, 5)
		if pct1 == 1 then
			local pct2 = number(1, 10)
			if pct2 == 1 then
				-- Našel jsi kliè 
				game.drop_item(30304, 1)
			else
				-- Našel jsi kliè  
				game.drop_item(30303, 1)
			end
		else
			return
		end
	end

	when 20366.click begin
		-- Budeš pøesunut do 9. patra.
		npc.purge()
		item.remove()
		timer("devil_jump_9", 6)
	end

	when devil_jump_9.timer begin
		d.setf("level", 9)
		d.jump_all(2048+590, 6656+155)
		d.regen_file("data/dungeon/deviltower9_regen.txt")
	end

	when 1093.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		d.kill_all()
		pc.give_item2(30320)
		say(" ")
		timer("devil_end_jump", 10)
	end

	when devil_end_jump.timer begin
		d.setf("level", 9)
		d.jump_all(2048+590, 6656+155)
		d.clear_regen()
		d.spawn_mob(1094, 605, 178)
	end
	
	when 1094.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		d.kill_all()
		timer("devil_end_jump_schmied", 10)
	end

	when devil_end_jump_schmied.timer begin
		d.setf("level", 9)
		d.jump_all(2048+590, 6656+155)
		d.clear_regen()
		d.spawn_mob(2598, 605, 178)
	end
	
	when 2598.kill with pc.in_dungeon() and pc.get_map_index() >= 660000 and pc.get_map_index() < 670000 begin
		d.notice("Vıbornì, dokázal jsi se dostat a na konec vìe,")
		d.notice("a proto tady na tebe èeká zbrojíø, platnéø a klenotník.")
		d.check_eliminated()
		d.kill_all()
		local reward_alchemist = {20074, 20075, 20076}
		d.spawn_mob(20074, 609, 179);
		d.spawn_mob(20075, 609, 172);
		d.spawn_mob(20076, 609, 185);
		d.spawn_mob(9012, 619, 170);
		d.setqf("can_refine", 1)
		timer("devil_end_sentinell", 150)
	end

	when devil_end_sentinell.timer begin
		d.exit_all()
		end
	end
end