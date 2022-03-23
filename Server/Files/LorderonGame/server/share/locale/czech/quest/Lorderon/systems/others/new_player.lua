quest novyhrac begin
    state start begin
        when login with pc.get_playtime() == 0 begin
            notice_all("Pøišel nový hráè: "..pc.get_name())
        end
    end
end