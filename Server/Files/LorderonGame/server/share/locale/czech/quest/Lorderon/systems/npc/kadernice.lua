quest kadernice begin 
    state start begin 
        when 20094.chat."��esy pro v�le�n�ky " begin  
            say_title("Kade�nice: ") 
            say("") 
            say("Chce� ��esy pro v�le�n�ky m�m jich spousty. ") 
			say("Chce� teda n�jak�? ")
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(8) 
            else 
                return 
            end 
        end 

        when 20094.chat."��esy pro Ninje " begin 
            say_title("Kade�nice: ") 
            say("") 
            say("Chce� ��esy pro ninje m�m jich spousty. ") 
			say("Chce� teda n�jak�? ") 
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(5) 
            else 
                return 
            end 
        end 
		
		when 20094.chat."��esy pro sury" begin 
            say_title("Kade�nice:") 
            say("") 
            say("Chce� ��esy pro sury m�m jich spousty. ") 
			say("Chce� teda n�jak�? ") 
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(6) 
            else 
                return 
            end 
        end 
		
		when 20094.chat."��esy pro �amany" begin 
            say_title("Kade�nice:") 
            say("") 
			say("Chce� ��esy pro �amany m�m jich spousty. ") 
			say("Chce� teda n�jak�? ")
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(7) 
            else 
                return 
            end 
        end
    end 
end  