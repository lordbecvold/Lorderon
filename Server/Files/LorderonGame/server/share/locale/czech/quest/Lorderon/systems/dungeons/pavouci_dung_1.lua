quest spider_dung_port begin
	state start begin
		when 20088.chat."Vstoupit do druh�ho patra(45-75 Lvl) " begin
			pc.warp(665600, 435200)	
		end
		when 20089.chat."Vstoupit do prvn�ho patra(35-45 Lvl) " begin
			pc.warp(51200, 486400)	
		end
	end
end
