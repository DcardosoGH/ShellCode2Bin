import sys
import binascii

def save_shellcode_to_bin(shellcode, output_file):
    shellcode_bytes = bytes(shellcode)
    
    with open(output_file, 'wb') as file:
        file.write(shellcode_bytes)
        

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: python3 ShellCode2Bin.py shellcode output_file")
        sys.exit(1)
        
    shellcode_str = sys.argv[1] 
    output_file = sys.argv[2]
    
    shellcode = [int(byte, 0) for byte in shellcode_str.split(',')]
    
    save_shellcode_to_bin(shellcode, output_file)
    print(f"ShellCode saved to {output_file}")