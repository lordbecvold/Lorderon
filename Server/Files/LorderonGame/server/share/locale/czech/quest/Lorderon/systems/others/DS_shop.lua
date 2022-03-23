define alchemist 20001
define dragon_soul_shop_vnum 9
quest dragon_soul_shop begin
	state start begin
		when alchemist.chat.gameforge.dragon_soul._100_npcChat with ds.is_qualified() begin
			npc.open_shop(dragon_soul_shop_vnum)
			setskin (NOWINDOW)
		end
	end
end
