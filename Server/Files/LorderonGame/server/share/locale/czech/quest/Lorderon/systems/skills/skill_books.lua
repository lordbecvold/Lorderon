quest techstufe begin 
    state start begin 
    function bookuse(book, skill) 
        local level = pc.get_skill_level(skill) 
        if level < 20 then 
            chat("Tuto Schopnost nemùžeš Trénovat. ") 
            return 
        end 
        if level > 29 then 
            chat("Tuto schopnost máš již na maximální úrovni. ") 
            return 
        end 
        pc.set_skill_level(skill, level+1) 
        pc.remove_item(book, 1)
        chat("Trénink probìhl úspìšnì. ") 
    end 
    when 50401.use begin techstufe.bookuse(50401, 1) end 
    when 50402.use begin techstufe.bookuse(50402, 2) end 
    when 50403.use begin techstufe.bookuse(50403, 3) end 
    when 50404.use begin techstufe.bookuse(50404, 4) end 
    when 50405.use begin techstufe.bookuse(50405, 5) end 
     
    when 50416.use begin techstufe.bookuse(50416, 16) end 
    when 50417.use begin techstufe.bookuse(50417, 17) end 
    when 50418.use begin techstufe.bookuse(50418, 18) end 
    when 50419.use begin techstufe.bookuse(50419, 19) end 
    when 50420.use begin techstufe.bookuse(50420, 20) end 
     
    when 50431.use begin techstufe.bookuse(50431, 31) end 
    when 50432.use begin techstufe.bookuse(50432, 32) end 
    when 50433.use begin techstufe.bookuse(50433, 33) end 
    when 50434.use begin techstufe.bookuse(50434, 34) end 
    when 50435.use begin techstufe.bookuse(50435, 35) end 
     
    when 50446.use begin techstufe.bookuse(50446, 46) end 
    when 50447.use begin techstufe.bookuse(50447, 47) end 
    when 50448.use begin techstufe.bookuse(50448, 48) end 
    when 50449.use begin techstufe.bookuse(50449, 49) end 
    when 50450.use begin techstufe.bookuse(50450, 50) end 
     
    when 50461.use begin techstufe.bookuse(50461, 61) end 
    when 50462.use begin techstufe.bookuse(50462, 62) end 
    when 50463.use begin techstufe.bookuse(50463, 63) end 
    when 50464.use begin techstufe.bookuse(50464, 64) end 
    when 50465.use begin techstufe.bookuse(50465, 65) end 
    when 50466.use begin techstufe.bookuse(50466, 66) end 
     
    when 50476.use begin techstufe.bookuse(50476, 76) end 
    when 50477.use begin techstufe.bookuse(50477, 77) end 
    when 50478.use begin techstufe.bookuse(50478, 78) end 
    when 50479.use begin techstufe.bookuse(50479, 79) end 
    when 50480.use begin techstufe.bookuse(50480, 80) end 
    when 50481.use begin techstufe.bookuse(50481, 81) end 
     
    when 50491.use begin techstufe.bookuse(50491, 91) end 
    when 50492.use begin techstufe.bookuse(50492, 92) end 
    when 50493.use begin techstufe.bookuse(50493, 93) end 
    when 50494.use begin techstufe.bookuse(50494, 94) end 
    when 50495.use begin techstufe.bookuse(50495, 95) end 
    when 50496.use begin techstufe.bookuse(50496, 96) end 
     
    when 50506.use begin techstufe.bookuse(50506, 106) end 
    when 50507.use begin techstufe.bookuse(50507, 107) end 
    when 50508.use begin techstufe.bookuse(50508, 108) end 
    when 50509.use begin techstufe.bookuse(50509, 109) end 
    when 50510.use begin techstufe.bookuse(50510, 110) end 
    when 50511.use begin techstufe.bookuse(50511, 111) end 
     
    end 
end  