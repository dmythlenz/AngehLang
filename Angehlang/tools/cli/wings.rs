use clap::Parser;  

#[derive(Parser)]  
struct Cli {  
    #[clap(subcommand)]  
    command: Command,  
}  

#[derive(Parser)]  
enum Command {  
    Build { target: Vec<String> },  
    Deploy { cloud: String },  
}  

fn main() {  
    let args = Cli::parse();  
    println!("✨ Breath successful!");  
}  