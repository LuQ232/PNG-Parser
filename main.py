import cv2
from decoder import Decoder
import argparse


"""READING PNG FILE"""
def init_png(image_path):
    png_file = open(path , 'rb')
    png_cv2_image = cv2.imread(image_path)

    #Check if file is png file
    if png_file.read(len(Decoder.SIGNATURE)) != Decoder.SIGNATURE:
        raise Exception('Its not PNG file')
    else:
        png_object = Decoder(png_file, png_cv2_image)

    return png_object

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="image file path")
    ap.add_argument("-l", "--chunk_list", nargs='?', const=True, default=False, help="chunks type list")
    ap.add_argument("-ihdr", "--ihdr", nargs='?', const=True, default=False, help="iHDR chunk")
    ap.add_argument("-srgb", "--srgb", nargs='?', const=True, default=False, help="sRGB chunk")
    ap.add_argument("-idat", "--idat", nargs='?', const=True, default=False, help="iDAT chunk")
    ap.add_argument("-iend", "--iend", nargs='?', const=True, default=False, help="iEND chunk")
    ap.add_argument("-gama", "--gama", nargs='?', const=True, default=False, help="gAMA chunk")
    ap.add_argument("-chrm", "--chrm", nargs='?', const=True, default=False, help="cHRM chunk")
    ap.add_argument("-plte", "--plte", nargs='?', const=True, default=False, help="pLTE chunk")
    ap.add_argument("-a", "--anonymization", nargs='?', const=True, default=False, help="proced anonymization")

    args = vars(ap.parse_args())
    path = args["path"]
    chunk_list = args["chunk_list"]
    ihdr = args["ihdr"]
    srgb = args["srgb"]
    idat = args["idat"]
    iend = args["iend"]
    gama = args["gama"]
    chrm = args["chrm"]
    plte = args["plte"]
    anonymization = args["anonymization"]

    png = init_png(path)
    if chunk_list:
        print("LISTA")
        png.print_chunks_type()
        print("-----------------------------\n")

    if ihdr:
        print("IHDR")
        png.IHDR_print_chunk_formated_data()
        print("-----------------------------\n")

    if srgb:
        print("SRGB")
        png.SRGB_print_chunk_data()
        print("-----------------------------\n")

    if idat:
        print("IDAT")
        png.IDAT_plot_image()
        print("-----------------------------\n")

    if iend:
        print("IEND")
        png.IEND_print_chunk_data()
        print("-----------------------------\n")

    if gama:
        print("GAMA")
        png.GAMA_print_chunk_formated_data()
        print("-----------------------------\n")

    if chrm:
        print("CHRM")
        png.CHRM_print_chunk_formated_data()
        print("-----------------------------\n")

    if plte:
        print("PLTE")
        png.PLTE_print_chunk_formated_data()
        print("-----------------------------\n")

    if anonymization:
        print("ANONYMIZATION")
        print("---")
        print("chunks before")
        png.print_chunks_type()
        print("---")

        path = png.anonymization()
        png2 = init_png(path)

        print("---")
        print("chunks after")
        png2.print_chunks_type()
        print("---")
        print("-----------------------------\n")
