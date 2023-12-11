def navigate_network(input_str, start, target, instructions):
    nodes = parse_nodes(input_str)
    current_node = start
    step_count = 0
    instruction_index = 0

    while current_node != target:
        instruction = instructions[instruction_index]
        instruction_index = (instruction_index + 1) % len(instructions)

        if instruction == 'L':
            current_node = nodes[current_node][0]
        elif instruction == 'R':
            current_node = nodes[current_node][1]

        step_count += 1

    return step_count
def parse_nodes(input_str):
    nodes = {}
    lines = input_str.strip().split('\n')
    for line in lines:
        parts = line.split(' = ')
        key = parts[0].strip()
        value = tuple(parts[1].strip('()').split(', '))
        nodes[key] = value
    return nodes

# Example usage
input_str = """
FLG = (PCR, CTD)
NNF = (CNH, SPV)
LDS = (FSN, SPM)
NMM = (CXD, LRK)
MHT = (TXF, KCB)
RRS = (BGH, HVX)
HLD = (LPJ, NGG)
GFB = (DSN, JFX)
PSS = (HDG, SMV)
XJC = (XMH, HGK)
FJP = (KJR, QHG)
VRS = (XKT, CPC)
KKM = (VGJ, KJF)
HNR = (KDB, PSK)
RXS = (NDK, RNH)
JKB = (RFF, TSX)
KRN = (BGQ, KGK)
BCV = (XKT, CPC)
JFV = (VCT, DJS)
FXP = (TLV, JDV)
QJX = (GHH, GSK)
CDR = (SGR, TQC)
CTD = (XBH, JJP)
PVN = (JVM, CSF)
NKR = (FHQ, SNF)
NDA = (MBM, SQN)
KCB = (JDG, CPB)
SJK = (JMT, JMT)
HVL = (RFQ, CTF)
RSK = (FXP, BJV)
TRN = (LVV, MSF)
NBN = (MPX, PTT)
QTJ = (BQD, DBR)
PJC = (MFL, TSD)
RFJ = (QJM, CVN)
FCV = (NQB, MJQ)
NML = (RTB, RTF)
KGV = (NGB, LDR)
KRC = (NHR, QCL)
GSK = (MCF, BRM)
NQB = (SJX, XBP)
TFG = (PDN, VGM)
XPB = (GMV, GDB)
RTJ = (SPK, HVR)
RFD = (VND, HVM)
KGK = (MHP, GMB)
MBX = (MPX, PTT)
NMC = (XVB, CCC)
SLC = (GNH, JHV)
QDG = (QSL, PJC)
MLB = (CXV, XBD)
PRH = (TFC, DNT)
TVN = (VXM, SLJ)
QXQ = (FLG, LJS)
TBB = (FVQ, FNC)
TLV = (PCS, SXL)
RSP = (CLL, TGG)
LPJ = (JNB, JBN)
MFL = (CNS, QTJ)
PHN = (HGN, PQS)
XBP = (MPS, TVN)
RSJ = (KVS, QDJ)
TVG = (GGG, QDD)
HGT = (BCV, VRS)
SMD = (VTP, MSR)
BLS = (NHR, QCL)
QVX = (DMJ, BND)
RBL = (MFT, JCG)
JCQ = (LGG, NFH)
DKN = (XSM, BQJ)
JFX = (XTJ, LNN)
QNB = (XNB, BJL)
TGG = (XVK, VQC)
PKV = (JXJ, QLQ)
KDB = (BQN, VGH)
HSX = (BCF, KPC)
XVB = (QKR, JCL)
KHB = (VFG, QVH)
HSG = (GDB, GMV)
NHT = (QLM, LHJ)
NFK = (KJD, FTH)
RFR = (XBD, CXV)
MFT = (RKT, SDL)
HVM = (MLB, RFR)
PJV = (XNX, LTD)
QBV = (XNB, BJL)
DBD = (RRG, RGJ)
MXD = (VRC, KNL)
JMT = (VFG, VFG)
SVS = (KXR, BGS)
RLT = (HVL, VDS)
JCL = (DHF, XTT)
RFK = (MCH, JBX)
QCJ = (VFM, SQL)
LVV = (SMQ, QDG)
VJG = (PXB, MCX)
CNP = (HBG, RGD)
JRT = (SGF, RGV)
CXB = (TRN, XGP)
PQR = (HVQ, VCJ)
TJC = (NNF, MNK)
PSP = (JCG, MFT)
RTF = (HDL, GGD)
NKK = (GPR, TMT)
KGB = (VLR, XQK)
DXF = (BXF, PBQ)
DLJ = (JXJ, QLQ)
CTF = (BDM, JNH)
GBL = (LBT, LBT)
KVN = (KDX, QMG)
VTB = (PNH, TDC)
XVK = (NHT, GTT)
HVR = (TBP, GSG)
VSF = (XJQ, LJC)
SPV = (KGT, XPR)
FTX = (KJD, FTH)
NPK = (XXQ, XVS)
KVS = (RKG, MKR)
SLG = (VXJ, BBV)
MCF = (XTV, LTK)
PBQ = (RLL, DHX)
JKS = (SSS, DRM)
JVR = (FJQ, PPK)
MKR = (LLQ, BMD)
DVX = (CHH, LBC)
LDV = (HFR, FVC)
DLP = (LXL, QJX)
TMG = (XMM, PLL)
KGM = (SXK, VTB)
JCK = (DBJ, HGT)
CMD = (JTH, MRV)
QCL = (PVN, NBF)
CNJ = (CFC, PKL)
TPM = (RSN, LXQ)
DMX = (RVK, FVK)
KNL = (SMD, HPJ)
JVM = (QSF, MMJ)
GGT = (GPR, TMT)
TFV = (QMH, DKN)
NQC = (HNR, FQD)
GNF = (TXF, KCB)
NMB = (QFL, FJP)
VTH = (XRX, DMH)
RQG = (VBK, KHL)
JBX = (TCR, JDN)
SSS = (DKX, LQS)
MPX = (GQC, VTH)
TVD = (XHT, HSS)
HVQ = (JPN, FLF)
PXL = (HMN, DLP)
QDJ = (MKR, RKG)
CLG = (TVG, CMZ)
XVP = (PVQ, PVQ)
MGM = (NVH, GFB)
CHL = (XVB, CCC)
NHR = (PVN, NBF)
FQX = (HLD, DXH)
HVX = (MFF, TFJ)
CNH = (XPR, KGT)
SFG = (MBX, NBN)
VXJ = (VSF, KBN)
RTL = (CFC, PKL)
BQN = (KLL, LDV)
KJR = (CQF, HLT)
DNT = (GBL, PGJ)
RKG = (BMD, LLQ)
HPX = (VGT, JFV)
DBM = (QBV, QNB)
MJQ = (XBP, SJX)
SQL = (BFD, FSK)
MJD = (XFD, JPP)
QXJ = (TVG, TVG)
DFN = (HVM, VND)
DPT = (NMF, PTS)
XNX = (RBS, TFV)
KPC = (PLM, PST)
NPB = (MRV, JTH)
TFJ = (SJJ, CXB)
QLM = (KGM, NCN)
FBG = (NCR, KGV)
QNP = (DHR, XPJ)
MNN = (HVQ, VCJ)
JDJ = (NPB, CMD)
VXP = (SNF, FHQ)
SXT = (HQK, BMS)
THQ = (SHM, XTR)
NGD = (BPR, PFK)
RBS = (QMH, DKN)
LHQ = (BCF, KPC)
BFD = (MJM, RVQ)
RFF = (LDX, CLK)
BCF = (PLM, PST)
BQD = (HSX, LHQ)
SBT = (JCQ, TTL)
JSN = (XQK, VLR)
VDS = (CTF, RFQ)
DHR = (LSB, KDH)
LGM = (JQX, JQX)
LTV = (CHL, NMC)
TMJ = (VGJ, KJF)
BVP = (DXF, CBJ)
GMB = (HMK, CMC)
DVK = (CXD, LRK)
RXP = (XTG, BQS)
HJH = (HNR, FQD)
PDL = (FCV, CRB)
SBL = (NQC, HJH)
DJS = (LTQ, FLP)
MSD = (TQC, SGR)
QHG = (CQF, HLT)
TQC = (SCQ, BVH)
NHK = (GPM, XVF)
TBP = (LJR, MJK)
KHT = (JFV, VGT)
PJH = (SFG, KBH)
DGN = (CNV, VHC)
KXT = (RXS, PDM)
GNH = (VCL, PXL)
MRV = (PGD, GBP)
SHS = (JMT, KHB)
JRH = (HPX, KHT)
NCR = (LDR, NGB)
BJN = (RQG, CSL)
RJJ = (RGV, SGF)
KFD = (FCV, CRB)
CRD = (CSL, RQG)
CSF = (QSF, MMJ)
CXD = (NKK, GGT)
GXG = (XMH, HGK)
RDD = (BMS, HQK)
JDV = (SXL, PCS)
XQQ = (FPS, KMS)
QJM = (JKQ, FQX)
JCG = (SDL, RKT)
FJD = (VXP, NKR)
LXF = (JVR, QMX)
CRB = (NQB, MJQ)
BLZ = (PRP, XRL)
QMH = (BQJ, XSM)
FBN = (SPM, FSN)
JFK = (QDJ, KVS)
SRM = (TJC, TGV)
TQT = (MHT, GNF)
XPJ = (LSB, KDH)
VRD = (MNN, PQR)
MMD = (RDT, XQJ)
BPX = (RPH, SVS)
DRF = (CNP, DKR)
MTX = (RTF, RTB)
GPT = (QRC, TPM)
QFL = (QHG, KJR)
AAA = (FKJ, QVX)
PGD = (DVX, QCR)
XSM = (FJB, PJH)
PDM = (NDK, RNH)
GJV = (QRC, TPM)
LBC = (QTQ, QSN)
XXQ = (KHC, LHG)
QLQ = (PMM, QNP)
CMC = (KKM, TMJ)
PMM = (DHR, XPJ)
MHP = (HMK, CMC)
FVK = (NHK, TDM)
LFM = (QMG, KDX)
VGT = (VCT, DJS)
VBR = (RBL, PSP)
KRV = (KVG, RDN)
GBP = (DVX, QCR)
DHF = (QXJ, QXJ)
PTA = (XRL, PRP)
GPR = (CTR, PSS)
LRK = (GGT, NKK)
DKX = (QCJ, LND)
JGB = (GNH, JHV)
SKF = (JBX, MCH)
JQX = (MBM, SQN)
JNB = (GXS, SBT)
TFC = (GBL, GBL)
DBG = (FLG, LJS)
SJC = (TGV, TJC)
SDL = (RSP, KHM)
KMR = (LGM, LGM)
LTK = (DBG, QXQ)
QSM = (KVN, LFM)
NFH = (RCT, BQT)
PCS = (DRF, TST)
JCN = (JRH, MNQ)
TTL = (NFH, LGG)
PQH = (XTR, SHM)
JBN = (SBT, GXS)
KBH = (MBX, NBN)
VXM = (SBL, KXX)
SCQ = (LDG, TFG)
RTB = (GGD, HDL)
MRF = (PDH, PXQ)
KLL = (FVC, HFR)
QMX = (PPK, FJQ)
VXQ = (RGJ, RRG)
BBV = (KBN, VSF)
NBF = (JVM, CSF)
XTG = (SLG, CMV)
XMF = (QJM, CVN)
DFB = (PBM, DMX)
PNH = (TBB, JSS)
XPR = (FBG, XXX)
JPP = (HHD, PVP)
XBH = (PKB, LTX)
XNB = (BGD, LPL)
RVB = (BMC, PRH)
HSS = (KMR, RLK)
GNG = (VQH, NMB)
LQS = (QCJ, LND)
BMD = (JRT, RJJ)
VFM = (BFD, FSK)
LXZ = (LQP, JBG)
MBH = (RPH, SVS)
QRC = (LXQ, RSN)
LLQ = (JRT, RJJ)
KBN = (LJC, XJQ)
SCR = (QLV, NRT)
SXL = (DRF, TST)
VGM = (GHN, FJD)
FLP = (NLN, PHN)
PFK = (RFJ, XMF)
BMS = (MMX, JDJ)
PNC = (KJV, NPK)
TTM = (JQX, RLZ)
LGG = (BQT, RCT)
VPM = (GNG, RTH)
BJL = (BGD, LPL)
CXV = (VKG, KHK)
RFQ = (BDM, JNH)
DQX = (JLX, RXP)
BGH = (TFJ, MFF)
HHD = (LHC, FHR)
SHM = (GVF, KXT)
HGK = (KRV, PNG)
BMC = (TFC, TFC)
MSR = (SRN, TQT)
KHL = (RFK, SKF)
XFD = (PVP, HHD)
FCK = (PVQ, GGC)
QCR = (CHH, LBC)
LTX = (MGM, VFD)
BGQ = (GMB, MHP)
XFJ = (NRT, QLV)
TGV = (NNF, MNK)
KXX = (HJH, NQC)
DKR = (RGD, HBG)
LND = (SQL, VFM)
DBR = (HSX, LHQ)
DJB = (MRF, PHJ)
VKG = (RTJ, HKL)
JPN = (KMT, TVD)
LNF = (FGQ, NTG)
NDK = (DFB, LLF)
MMJ = (RQH, QSG)
NMF = (LJT, BPS)
JMF = (SRM, SJC)
RGV = (MBH, BPX)
MBM = (XNR, VJK)
JGT = (CQT, LXF)
XTT = (QXJ, CLG)
SLJ = (SBL, KXX)
JNC = (NMF, PTS)
VJK = (HVG, LDT)
XQK = (BTX, QLN)
SNR = (DTS, LNF)
MQR = (FGG, CCV)
VCJ = (JPN, FLF)
QTN = (VRC, KNL)
RLZ = (SQN, MBM)
FNC = (SRX, JQD)
GCD = (DLJ, PKV)
SQT = (PKV, DLJ)
LHC = (MMD, CNR)
HGN = (QJH, BMR)
QSL = (TSD, MFL)
BGS = (DVK, NMM)
CCC = (QKR, JCL)
TSX = (CLK, LDX)
PRP = (MJD, XMS)
RCT = (KRC, BLS)
QMM = (XNN, QSM)
MCX = (SGP, PJV)
SQN = (XNR, VJK)
BVH = (TFG, LDG)
VFD = (GFB, NVH)
SCV = (SJC, SRM)
TDM = (XVF, GPM)
DTS = (FGQ, NTG)
RDT = (RNF, RLT)
HKL = (SPK, HVR)
TCK = (TSX, RFF)
HDL = (BNL, RRS)
CVN = (FQX, JKQ)
PBA = (DFN, RFD)
PGJ = (LBT, BLZ)
DPM = (MNN, PQR)
KHC = (QMM, KVL)
BRM = (LTK, XTV)
VTP = (TQT, SRN)
DBJ = (VRS, BCV)
JTP = (VHC, CNV)
HMK = (TMJ, KKM)
JQD = (GCD, SQT)
QDD = (TNT, VJG)
FQD = (KDB, PSK)
QLV = (VBR, BXG)
LXL = (GHH, GSK)
MMX = (NPB, CMD)
VFG = (MKX, MKX)
PDH = (NHJ, LTV)
RGJ = (DQX, VLD)
NHJ = (CHL, NMC)
NLN = (HGN, PQS)
LTQ = (NLN, PHN)
RRG = (DQX, VLD)
VHC = (SXT, RDD)
VGJ = (QMC, TMG)
HFR = (JCN, RNJ)
GGC = (JHJ, MNP)
QLN = (NNM, PNC)
XTV = (QXQ, DBG)
QCN = (SSS, DRM)
LJS = (PCR, CTD)
GMV = (HQM, KRN)
JDN = (RSK, SLM)
SMQ = (PJC, QSL)
LJC = (SMH, VPM)
CHH = (QTQ, QSN)
CMZ = (QDD, GGG)
CDC = (BPR, PFK)
NCN = (SXK, VTB)
GHH = (BRM, MCF)
MNQ = (HPX, KHT)
JLX = (BQS, XTG)
VND = (RFR, MLB)
QMC = (XMM, PLL)
BPS = (JFK, RSJ)
SNF = (XPB, HSG)
BPR = (XMF, RFJ)
JHJ = (DHH, DHH)
XKT = (NFK, FTX)
BDM = (PDL, KFD)
GHN = (NKR, VXP)
RTH = (VQH, NMB)
SGR = (SCQ, BVH)
MNK = (CNH, SPV)
QKR = (DHF, DHF)
HLT = (XVP, FCK)
JJP = (LTX, PKB)
NGB = (JSN, KGB)
BXB = (LNF, DTS)
RVQ = (QQM, XQQ)
PLL = (DBD, VXQ)
XDL = (CBJ, DXF)
KJF = (QMC, TMG)
VQH = (QFL, FJP)
RKT = (RSP, KHM)
VFL = (PHJ, MRF)
MNP = (DHH, ZZZ)
LHJ = (NCN, KGM)
DMH = (KNV, MKP)
RLL = (SCR, XFJ)
BNL = (BGH, HVX)
XLB = (JCK, MXG)
PCR = (JJP, XBH)
KDH = (DJB, VFL)
XTR = (GVF, KXT)
PSK = (VGH, BQN)
DVA = (JBG, LQP)
MFF = (CXB, SJJ)
GQC = (XRX, DMH)
CFC = (TCK, JKB)
RNJ = (MNQ, JRH)
BND = (KCQ, JGT)
GXS = (TTL, JCQ)
LDR = (JSN, KGB)
CQF = (XVP, FCK)
BJV = (TLV, JDV)
KXR = (DVK, NMM)
PBM = (FVK, RVK)
MJM = (XQQ, QQM)
LLF = (PBM, DMX)
MKP = (NGV, KHN)
XMM = (DBD, VXQ)
MNT = (DFN, RFD)
FGG = (JTP, DGN)
XRX = (MKP, KNV)
CLK = (GXG, XJC)
CPM = (NGD, CDC)
SGF = (MBH, BPX)
MXG = (HGT, DBJ)
SDS = (QNB, QBV)
NNM = (NPK, KJV)
BXG = (PSP, RBL)
SXK = (PNH, TDC)
PQS = (QJH, BMR)
FSK = (MJM, RVQ)
CPC = (FTX, NFK)
KVL = (XNN, QSM)
JDG = (GPT, GJV)
XRL = (MJD, XMS)
HPJ = (VTP, MSR)
CBJ = (BXF, PBQ)
PDN = (GHN, FJD)
SGP = (XNX, LTD)
QVH = (MKX, LXZ)
RNF = (HVL, VDS)
CLL = (XVK, VQC)
QSF = (RQH, QSG)
PKB = (VFD, MGM)
KHN = (BVP, XDL)
KJD = (RTL, CNJ)
VRC = (HPJ, SMD)
FTH = (RTL, CNJ)
BQS = (SLG, CMV)
LCP = (MNT, MNT)
GVF = (RXS, PDM)
LNN = (MBC, XDQ)
LJR = (MXD, QTN)
XJQ = (VPM, SMH)
DHH = (FKJ, QVX)
FVC = (JCN, RNJ)
GPM = (SNR, BXB)
QSG = (JNC, DPT)
CNV = (RDD, SXT)
FLF = (KMT, TVD)
PNG = (KVG, RDN)
FVQ = (JQD, SRX)
TXF = (JDG, CPB)
XTJ = (XDQ, MBC)
HVG = (FRN, MQR)
PXB = (PJV, SGP)
PTS = (BPS, LJT)
TMT = (CTR, PSS)
GDB = (KRN, HQM)
HMN = (LXL, QJX)
VQC = (NHT, GTT)
HDG = (LCP, LCP)
KHK = (HKL, RTJ)
FRN = (FGG, CCV)
FKJ = (DMJ, BND)
PVJ = (NGD, CDC)
PVQ = (JHJ, JHJ)
SLM = (BJV, FXP)
MSF = (QDG, SMQ)
SPK = (TBP, GSG)
PPK = (MSD, CDR)
CCV = (DGN, JTP)
TDC = (TBB, JSS)
PLM = (RVB, PXV)
MKX = (JBG, LQP)
PMZ = (RFD, DFN)
RPH = (KXR, BGS)
JSS = (FVQ, FNC)
XVF = (SNR, BXB)
SMV = (LCP, VPH)
KMS = (LDS, FBN)
KJV = (XVS, XXQ)
SRX = (GCD, SQT)
GTT = (QLM, LHJ)
DMJ = (KCQ, JGT)
LQP = (PQH, THQ)
BMR = (SLC, JGB)
VPH = (MNT, PMZ)
SMH = (GNG, RTH)
XXX = (KGV, NCR)
PKL = (TCK, JKB)
XVS = (LHG, KHC)
HCA = (GGG, QDD)
LHG = (QMM, KVL)
KMT = (XHT, HSS)
CNS = (BQD, DBR)
CQT = (QMX, JVR)
FSN = (SDS, DBM)
QMG = (XLB, TKJ)
QQM = (KMS, FPS)
RQH = (JNC, DPT)
NGV = (XDL, BVP)
XMH = (KRV, PNG)
JXJ = (QNP, PMM)
RGD = (JKS, QCN)
LDG = (VGM, PDN)
DHX = (XFJ, SCR)
XBD = (VKG, KHK)
MBC = (MTX, NML)
SKK = (SJK, SHS)
XDQ = (MTX, NML)
VGH = (KLL, LDV)
VLD = (RXP, JLX)
KVG = (DPM, VRD)
LTD = (RBS, TFV)
FHR = (MMD, CNR)
PXV = (BMC, PRH)
KHM = (TGG, CLL)
GGG = (TNT, VJG)
TNT = (PXB, MCX)
FPS = (FBN, LDS)
PVP = (FHR, LHC)
CMV = (VXJ, BBV)
RSN = (CPM, PVJ)
NTG = (BJN, CRD)
BQJ = (FJB, PJH)
SJX = (MPS, TVN)
LPL = (SKK, HTT)
CPB = (GJV, GPT)
DRM = (DKX, LQS)
XQJ = (RLT, RNF)
CSL = (VBK, KHL)
TCR = (RSK, SLM)
DSN = (XTJ, LNN)
VCT = (FLP, LTQ)
JHV = (VCL, PXL)
PXQ = (NHJ, LTV)
LSB = (VFL, DJB)
VBK = (SKF, RFK)
NVH = (JFX, DSN)
GGD = (RRS, BNL)
LDX = (XJC, GXG)
FJB = (SFG, KBH)
LDT = (MQR, FRN)
QSN = (SCV, JMF)
BGD = (SKK, HTT)
GSG = (MJK, LJR)
CNR = (XQJ, RDT)
NRT = (VBR, BXG)
NGG = (JBN, JNB)
ZZZ = (QVX, FKJ)
FGQ = (BJN, CRD)
KNV = (KHN, NGV)
XNR = (HVG, LDT)
PHJ = (PDH, PXQ)
LBT = (XRL, PRP)
HQK = (MMX, JDJ)
BXF = (RLL, DHX)
TKJ = (MXG, JCK)
SJJ = (TRN, XGP)
HBG = (JKS, QCN)
KCQ = (LXF, CQT)
XMS = (XFD, JPP)
LXQ = (CPM, PVJ)
JTH = (GBP, PGD)
RLK = (LGM, TTM)
TST = (DKR, CNP)
BQT = (KRC, BLS)
VCL = (HMN, DLP)
RDN = (VRD, DPM)
XGP = (MSF, LVV)
KGT = (XXX, FBG)
HTT = (SJK, SHS)
PST = (RVB, PXV)
JKQ = (DXH, HLD)
JNH = (PDL, KFD)
RNH = (LLF, DFB)
KDX = (XLB, TKJ)
PTT = (GQC, VTH)
FHQ = (XPB, HSG)
XNN = (LFM, KVN)
MCH = (JDN, TCR)
MPS = (VXM, SLJ)
BTX = (NNM, PNC)
CTR = (HDG, HDG)
QJH = (JGB, SLC)
SPM = (SDS, DBM)
FJQ = (CDR, MSD)
DXH = (NGG, LPJ)
VLR = (BTX, QLN)
SRN = (GNF, MHT)
MJK = (QTN, MXD)
QTQ = (SCV, JMF)
HQM = (KGK, BGQ)
RVK = (TDM, NHK)
JBG = (THQ, PQH)
TSD = (CNS, QTJ)
LJT = (RSJ, JFK)
XHT = (KMR, KMR)
"""
nodes = parse_nodes(input_str)

# Using the new function
instructions = "LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"
start_node = 'AAA'  # example start node
target_node = 'ZZZ'  # example target node

steps = navigate_network(input_str, start_node, target_node, instructions)
print(f"Steps required to reach {target_node}: {steps}")
