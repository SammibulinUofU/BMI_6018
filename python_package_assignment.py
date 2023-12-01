import pysam

# Using the pysam package to analyze the BAM flags reported in the ERR188273_chrX.bam file


alignment_file = pysam.AlignmentFile("ERR188273_chrX.bam", "rb")

BAM_Flag_Report = {}

for line1 in alignment_file:
	line2 = next(alignment_file)
	line1 = str(line1)
	line2 = str(line2)
	line1_els = line1.split("\t")
	line2_els = line2.split("\t")
	
	bam_flag_1 = line1_els[1]
	bam_flag_2 = line2_els[1]

	if bam_flag_1 in BAM_Flag_Report.keys():
		BAM_Flag_Report[bam_flag_1] += 1
	else:
		BAM_Flag_Report[bam_flag_1] = 1

	if bam_flag_2 in BAM_Flag_Report.keys():
		BAM_Flag_Report[bam_flag_2] += 1
	else:
		BAM_Flag_Report[bam_flag_2] = 1

print(BAM_Flag_Report)	
	
