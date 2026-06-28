#!/usr/bin/ruby
class Kaibro
    def initialize name
        @name = name
    end

    def name
        @name
    end
end

c = gets("*").strip
t = Marshal.load(c)
puts `#{t.name}`
