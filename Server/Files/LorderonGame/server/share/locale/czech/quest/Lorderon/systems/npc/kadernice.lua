quest kadernice begin 
    state start begin 
        when 20094.chat."Úèesy pro váleèníky " begin  
            say_title("Kadeønice: ") 
            say("") 
            say("Chceš úèesy pro váleèníky mám jich spousty. ") 
			say("Chceš teda nìjaký? ")
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(8) 
            else 
                return 
            end 
        end 

        when 20094.chat."Úèesy pro Ninje " begin 
            say_title("Kadeønice: ") 
            say("") 
            say("Chceš úèesy pro ninje mám jich spousty. ") 
			say("Chceš teda nìjaký? ") 
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(5) 
            else 
                return 
            end 
        end 
		
		when 20094.chat."Úèesy pro sury" begin 
            say_title("Kadeønice:") 
            say("") 
            say("Chceš úèesy pro sury mám jich spousty. ") 
			say("Chceš teda nìjaký? ") 
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(6) 
            else 
                return 
            end 
        end 
		
		when 20094.chat."Úèesy pro šamany" begin 
            say_title("Kadeønice:") 
            say("") 
			say("Chceš úèesy pro šamany mám jich spousty. ") 
			say("Chceš teda nìjaký? ")
            local r = select("Ano", "Ne") 
            if r == 1 then 
                npc.open_shop(7) 
            else 
                return 
            end 
        end
    end 
end  