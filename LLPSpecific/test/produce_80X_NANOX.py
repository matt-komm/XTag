# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test80X -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --filein /store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/120000/02A210D6-F5C3-E611-B570-008CFA197BD4.root --no_exec --conditions auto:run2_mc -n 1000 --era Run2_2016,run2_miniAOD_80XLegacy
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

from Configuration.StandardSequences.Eras import eras


options = VarParsing ('analysis')

options.register(
    'isData',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "is data"
)

options.register(
    'addLLPInfo',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "add llp info"
)

options.register(
    'noFilter',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "apply no filtering"
)

options.parseArguments()



process = cms.Process('NANO',eras.Run2_2016,eras.run2_miniAOD_80XLegacy)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring()
)

if options.isData:
    process.source.fileNames = [
        '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver2-v1/110000/F836EEF3-E8EA-E611-AB15-0CC47AA9943A.root'
    ]
else:
    process.source.fileNames = [
        #'file:DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'
        #'/store/mc/RunIISummer16MiniAODv2/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2C548AA6-91CF-E611-A86B-B083FED429D6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/SMS-T1qqqq_ctau-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_GridpackScan_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/10000/000486C0-2588-E711-8E92-0025905A48BA.root',
  	    #'root://cmsxrootd.fnal.gov//store/mc/RunIISummer16MiniAODv2/SMS-T1qqqq_ctau-0p01_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_GridpackScan_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/0C07E448-338A-E711-B877-0CC47A4D75F2.root'
  	    #"root://cmsxrootd.fnal.gov//store/mc/RunIISummer16MiniAODv2/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/04915DCA-1BB2-E611-8A4B-0CC47A4C8E56.root"
  	    #"root://cmsxrootd.fnal.gov//store/mc/RunIISummer16MiniAODv2/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/00898E1E-99B1-E611-8A4A-C81F66C8BA4C.root",
  	    #"/store/mc/RunIISummer16MiniAODv2/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/00E276CA-A6B6-E611-9C22-3417EBE47EBC.root",
    ]
    

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    #allowUnscheduled = cms.untracked.bool(True) 
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('test80X nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

process.plain=cms.Path()
process.filteredSingleMuCR=cms.Path()
process.filteredSingleEleCR=cms.Path()


def addModule(m):
    process.plain+=m
    process.filteredSingleMuCR+=m
    process.filteredSingleEleCR+=m

### selectors ###
skimSingleMuSequence = cms.Sequence()
process.filteredSingleMuCR+=skimSingleMuSequence
skimSingleEleSequence = cms.Sequence()
process.filteredSingleEleCR+=skimSingleEleSequence


def addFilter(seq,inputTag,cutString,minN=None):
    name = str(inputTag._InputTag__moduleLabel)
    
    if minN!=None:
        name+="min"+str(minN)
        
    selector = cms.EDFilter("CandViewSelector",
        src = inputTag,
        cut = cms.string(cutString)
    )
    selectorName="select"+name
    setattr(process,selectorName,selector)
    seq+=selector
  
    if minN!=None:
        selectorMinFilter = cms.EDFilter("CandViewCountFilter",
            src = cms.InputTag(selectorName),
            minNumber = cms.uint32(minN)
        )
        selectorMinFilterName="minFilter"+name
        setattr(process,selectorMinFilterName,selectorMinFilter)
        seq+=selectorMinFilter
        
        
if not options.noFilter:
    addFilter(skimSingleMuSequence,cms.InputTag("slimmedMuons"),"pt>24.0",minN=1)
    addFilter(skimSingleMuSequence,cms.InputTag("slimmedJets"),"pt>20.0",minN=1)
    
    addFilter(skimSingleEleSequence,cms.InputTag("slimmedElectrons"),"pt>27.0",minN=1)
    addFilter(skimSingleEleSequence,cms.InputTag("slimmedJets"),"pt>20.0",minN=1)

'''
if not options.isData:
    process.TFileService = cms.Service("TFileService", 
        fileName = cms.string("info.root")
    )

    process.eventAndPuInfo = cms.EDAnalyzer("EventInfoCollector",
        GenEventInfo=cms.InputTag("generator"),
        PileupSummaryInfo=cms.InputTag("slimmedAddPileupInfo")
    )
    process.plain+=process.eventAndPuInfo
'''
# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    saveProvenance = cms.untracked.bool(True),
    fakeNameForCrab = cms.untracked.bool(True),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring([
            "filtered*",
            "plain*", #this deactivates filtering
        ])
    ), 
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('nano.root'),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep nanoaodFlatTable_*Table_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep nanoaodMergeableCounterTable_*Table_*_*', 
        'keep nanoaodUniqueString_nanoMetadata_*_*',
        
        'drop *_caloMetTable_*_*',
        'drop *_fatJetTable_*_*',
        'drop *_genJetAK8FlavourTable_*_*',
        'drop *_genJetAK8Table_*_*',
        'drop *_genVisTauTable_*_*',
        'drop *_subJetTable_*_*',
        'drop *_tkMetTable_*_*',
        'drop *_puppiMetTable_*_*',
        'drop *_ttbarCategoryTable_*_*',
        
        'drop *_photonTable_*_*',
        'drop *_photonMCTable_*_*',
        
        'drop *_tauTable_*_*',
        'drop *_tauMCTable_*_*' ,
        
        'drop *_saJetTable_*_*',
        'drop *_saTable_*_*',
        
        'drop *_simpleCleanerTable_photons_*',
        'drop *_simpleCleanerTable_taus_*',
        
        'drop *_rivetMetTable_*_*',
        'drop *_rivetLeptonTable_*_*',
        
    )
)
'''
process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('output.root'),
    outputCommands = cms.untracked.vstring(
        "keep *",
        
     ),#+process.NANOAODSIMoutput.outputCommands,
    dropMetaData = cms.untracked.string('ALL'),
)
'''

from Configuration.AlCa.GlobalTag import GlobalTag
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
if options.isData:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data_relval', '')
    jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'], 'None')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
    jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
    
bTagInfos = [
    'pfImpactParameterTagInfos',
    'pfInclusiveSecondaryVertexFinderTagInfos',
    'pfDeepCSVTagInfos',
]
bTagDiscriminators = [
    #'softPFMuonBJetTags',
    #'softPFElectronBJetTags',
    #'pfJetBProbabilityBJetTags',
    #'pfJetProbabilityBJetTags',
    'pfCombinedInclusiveSecondaryVertexV2BJetTags',
    'pfDeepCSVJetTags:probudsg', #to be fixed with new names
    'pfDeepCSVJetTags:probb',
    'pfDeepCSVJetTags:probc',
    'pfDeepCSVJetTags:probbb',
    #'pfDeepCSVJetTags:probcc',
]
updateJetCollection(
        process,
        labelName = "XTag",
        jetSource = cms.InputTag('slimmedJets'),#'ak4Jets'
        jetCorrections = jetCorrectionsAK4,
        pfCandidates = cms.InputTag('packedPFCandidates'),
        pvSource = cms.InputTag("offlineSlimmedPrimaryVertices"),
        svSource = cms.InputTag('slimmedSecondaryVertices'),
        muSource = cms.InputTag('slimmedMuons'),
        elSource = cms.InputTag('slimmedElectrons'),
        btagInfos = bTagInfos,
        btagDiscriminators = bTagDiscriminators,
        explicitJTA = False,
)
#there seems to be a bug: addTagInfos is set to false despite len(btagInfos)>0
#to be sure specify included information explicitly here
process.updatedPatJetsTransientCorrectedXTag.addBTagInfo = cms.bool(True)
process.updatedPatJetsTransientCorrectedXTag.addDiscriminators = cms.bool(True)
process.updatedPatJetsTransientCorrectedXTag.addJetCorrFactors = cms.bool(True)
process.updatedPatJetsTransientCorrectedXTag.addTagInfos = cms.bool(True)


process.updateJetXTagSequence = cms.Sequence(
    process.patJetCorrFactorsXTag
    +process.updatedPatJetsXTag
    +process.pfImpactParameterTagInfosXTag
    +process.pfInclusiveSecondaryVertexFinderTagInfosXTag
    +process.pfDeepCSVTagInfosXTag
    +process.pfDeepCSVJetTagsXTag
    +process.pfCombinedInclusiveSecondaryVertexV2BJetTagsXTag
    +process.patJetCorrFactorsTransientCorrectedXTag
    +process.updatedPatJetsTransientCorrectedXTag
)
addModule(process.updateJetXTagSequence)

process.selectJetsInBarrel = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("updatedPatJetsTransientCorrectedXTag"),
    cut = cms.string("pt > 20")
)
addModule(process.selectJetsInBarrel)

process.xtagProducer = cms.EDProducer("XTagProducer",
    plugins = cms.PSet(
        globalVars = cms.PSet(
            type = cms.string("GlobalJetTagData"),
            #src = cms.InputTag("linkedObjects","jets")
            jets = cms.InputTag("selectJetsInBarrel"),
        ),
        csv = cms.PSet(
            type = cms.string("CSVInputTagData"),
            jets = cms.InputTag("selectJetsInBarrel"),
            tagName = cms.string('pfDeepCSV')
        ),
        cpf = cms.PSet(
            type = cms.string("ChargedPFTagData"),
            jets = cms.InputTag("selectJetsInBarrel"),
            pvVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
            svVertices = cms.InputTag("slimmedSecondaryVertices"),
        ),
        npf = cms.PSet(
            type = cms.string("NeutralPFTagData"),
            jets = cms.InputTag("selectJetsInBarrel"),
            svVertices = cms.InputTag("slimmedSecondaryVertices"),
        ),
        sv = cms.PSet(
            type = cms.string("SVTagData"),
            jets = cms.InputTag("selectJetsInBarrel"),
            pvVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
            svVertices = cms.InputTag("slimmedSecondaryVertices"),
        ),
        
    )
)

process.xtagFlatTable = cms.EDProducer("XTagFlatTableProducer",
    tagData = cms.VPSet([
        cms.PSet(
            src = cms.InputTag("xtagProducer","globalVars"),
            arrayNames = cms.vstring(["global"])
        ),
        cms.PSet(
            src = cms.InputTag("xtagProducer","csv"),
            arrayNames = cms.vstring(["csv"])
        ),
        cms.PSet(
            src = cms.InputTag("xtagProducer","cpf"),
            arrayNames = cms.vstring(["cpflength","cpf"])
        ),
        cms.PSet(
            src = cms.InputTag("xtagProducer","npf"),
            arrayNames = cms.vstring(["npflength","npf"])
        ),
        cms.PSet(
            src = cms.InputTag("xtagProducer","sv"),
            arrayNames = cms.vstring(["svlength","sv"])
        ),
        
    ])
)

if not options.isData:
    process.xtagProducer.plugins.origin = cms.PSet(
        type = cms.string("JetOriginTagData"),
        jets = cms.InputTag("selectJetsInBarrel"),
        displacedGenVertices = cms.InputTag("displacedGenVertices"),
    )
    
    process.xtagFlatTable.tagData.append(cms.PSet(
        src = cms.InputTag("xtagProducer","origin"),
        arrayNames = cms.vstring(["jetorigin"])
    ))
    
    if options.addLLPInfo:
        process.xtagProducer.plugins.llpinfo = cms.PSet(
            type = cms.string("LLPInfo"),
            displacedGenVertices = cms.InputTag("displacedGenVertices"),
        )
        process.xtagFlatTable.tagData.append(cms.PSet(
            src = cms.InputTag("xtagProducer","llpinfo"),
            arrayNames = cms.vstring(["llpinfo"])
        ))
    
#process.eventView = cms.EDAnalyzer(
#    "EventViewer",
#    genParticles = cms.InputTag("genParticlesMerged"),
#    genJets = cms.InputTag("genJetsReclustered"),
#    selection = cms.string('(abs(pdgId)<6) && (abs(mother.pdgId)==1000021)')
#)

#remove unneeded modules
    for moduleName in [
        "chsForSATkJets",
        "softActivityJets",
        "softActivityJets2",
        "softActivityJets5",
        "softActivityJets10",
        
        "fatJetTable",
        "subJetTable",
        "saJetTable",
        "saTable",
        
        "genJetAK8Table",
        "genJetAK8FlavourAssociation",
        "genJetAK8FlavourTable",
       
        "particleLevel",
        "rivetLeptonTable",
        "rivetMetTable"
    ]:
        if hasattr(process,moduleName):
            print "removing module: ",moduleName
            if options.isData:
                process.nanoSequence.remove(getattr(process,moduleName))
            else:
                process.nanoSequenceMC.remove(getattr(process,moduleName))
            
if options.isData:
    addModule(process.nanoSequence)
else:
    addModule(process.nanoSequenceMC)

if not options.isData:
    process.load('XTag.DisplacedVertex.GenDisplacedVertices_cff')
    addModule(process.DisplacedGenVertexSequence)

process.nanoxSequence = cms.Sequence( 
    process.xtagProducer
    +process.xtagFlatTable
    #+process.eventView
)
addModule(process.nanoxSequence)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(
    process.NANOAODSIMoutput
    #+process.MINIAODoutput
)

# Schedule definition
#process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
#from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
#associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeData,nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
if options.isData:
    process = nanoAOD_customizeData(process)
else:
    process = nanoAOD_customizeMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
