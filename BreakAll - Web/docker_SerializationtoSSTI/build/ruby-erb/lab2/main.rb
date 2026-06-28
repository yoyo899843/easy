require 'sinatra'
set :bind, '0.0.0.0'
set :port, 11111
get '/' do
 erb :home
end
 
get '/about' do
 erb :about
end

get '/article/:id' do
 erb("Article id: ('#{params[:id]}') not found!", :layout => false)
end

get '/flag' do
 erb :flag
end

get '/source' do
 File.open(__FILE__, 'r').read
end
