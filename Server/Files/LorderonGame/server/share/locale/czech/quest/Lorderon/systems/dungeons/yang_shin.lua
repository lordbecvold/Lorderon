quest yang_shin begin
	state start begin
		when 20019.chat."Opi�� jeskyn� (30-55 Lvl) " begin
		if pc.get_level() < 30 then
			say_title(" Str�ce opi�� jeskyn� ")
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 55 then
			say_title(" Str�ce opi�� jeskyn� ")
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(768000, 435200)	
			end
		end
		when 20019.chat."Opi�� jeskyn� 2 (55-75 Lvl) " begin
		if pc.get_level() < 55 then
			say_title(" Str�ce opi�� jeskyn� ")
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 75 then
			say_title(" Str�ce opi�� jeskyn� ")
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(128000, 640000)	
			end
		end
		when 20019.chat."Opi�� jeskyn� 3 (75-95 Lvl) " begin
		if pc.get_level() < 75 then
			say_title(" Str�ce opi�� jeskyn� ")
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 95 then
			say_title(" Str�ce opi�� jeskyn� ")
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(128000, 716800)	
			end
		end
		when 20019.chat."Dra�� chr�m (75-105 Lvl) " begin
		if pc.get_level() < 75 then
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 105 then
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(819200, 1049600)	
			end
		end
		when 20019.chat."V� d�mon� (40-105 Lvl) " begin
		if pc.get_level() < 40 then
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 105 then
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(590500, 110500)	
			end
		end
		when 20019.chat."Razadorova pevnost (100-120 Lvl) " begin
		if pc.get_level() < 100 then
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 120 then
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(742400, 614400)	
			end
		end
		when 20019.chat."Nemerova pevnost (100-120 Lvl) " begin
		if pc.get_level() < 100 then
			say(" Tv� �roveo je po�li� n�zk� ")
		elseif pc.get_level() > 120 then
			say(" Tv� �roveo je po�li� vysok� ")
		else
			pc.warp(512000, 153600)	
			end
		end
	end
end