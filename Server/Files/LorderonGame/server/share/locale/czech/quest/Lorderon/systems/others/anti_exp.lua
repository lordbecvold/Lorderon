quest antiexp begin
    state start begin
        when login begin
            if pc.getqf("antiexp") == 1 then
                pc.block_exp()
                chat("Zisk zku�enost� byl pozastaven. ")
            end
        end
        when 30201.use begin
            if pc.getqf("antiexp") == 0 then
                pc.block_exp()
                pc.setqf("antiexp", 1)
                chat("Zisk zku�enost� byl pozastaven. ")
            elseif pc.getqf("antiexp") == 1 then
                pc.unblock_exp()
                pc.setqf("antiexp", 0)
                chat("Zisk zku�enost� byl povolen. ")
            end
        end
    end
end
